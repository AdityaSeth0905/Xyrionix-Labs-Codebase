import json
import logging
from typing import Dict, Any, Optional
import requests
from enum import Enum, auto
from dataclasses import dataclass, field
from datetime import datetime
import uuid

class WebhookType(Enum):
    """
    Enumeration of different webhook types
    """
    GENERIC = auto()
    EMAIL_NOTIFICATION = auto()
    USER_ACTIVITY = auto()
    SYSTEM_ALERT = auto()
    SECURITY_EVENT = auto()

@dataclass
class Webhook:
    """
    Webhook model for managing and sending webhook notifications
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ''
    url: str = ''
    type: WebhookType = WebhookType.GENERIC
    secret_key: Optional[str] = None
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_sent: Optional[datetime] = None
    retry_count: int = 0
    max_retries: int = 3

    def validate_url(self) -> bool:
        """
        Validate webhook URL
        
        Returns:
            bool: Whether URL is valid
        """
        try:
            # Basic URL validation
            import validators
            return validators.url(self.url)
        except ImportError:
            # Fallback validation if validators not installed
            import re
            url_pattern = re.compile(
                r'^https?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            return bool(url_pattern.match(self.url))

class WebhookDispatcher:
    """
    Handles webhook dispatching and management
    """
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize WebhookDispatcher
        
        Args:
            logger (logging.Logger, optional): Custom logger
        """
        self.logger = logger or logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )

    def _generate_signature(self, payload: Dict[str, Any], secret_key: Optional[str]) -> Optional[str]:
        """
        Generate webhook signature for security
        
        Args:
            payload (dict): Webhook payload
            secret_key (str, optional): Secret key for signing
        
        Returns:
            str or None: Generated signature
        """
        if not secret_key:
            return None
        
        import hashlib
        import hmac
        
        payload_json = json.dumps(payload, sort_keys=True)
        signature = hmac.new(
            secret_key.encode('utf-8'), 
            payload_json.encode('utf-8'), 
            hashlib.sha256
        ).hexdigest()
        
        return signature

    def send_webhook(self, webhook: Webhook, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send webhook notification
        
        Args:
            webhook (Webhook): Webhook configuration
            payload (dict): Payload to send
        
        Returns:
            dict: Webhook sending result
        """
        # Validate webhook
        if not webhook.is_active:
            self.logger.warning(f"Webhook {webhook.id} is not active")
            return {'status': 'error', 'message': 'Webhook is not active'}

        if not webhook.validate_url():
            self.logger.error(f"Invalid webhook URL: {webhook.url}")
            return {'status': 'error', 'message': 'Invalid webhook URL'}

        # Prepare headers
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'WebhookDispatcher/1.0'
        }

        # Add signature if secret key exists
        signature = self._generate_signature(payload, webhook.secret_key)
        if signature:
            headers['X-Webhook-Signature'] = signature

        try:
            # Send webhook
            response = requests.post(
                webhook.url, 
                data=json.dumps(payload),
                headers=headers,
                timeout=10
            )
            
            # Check response
            response.raise_for_status()
            
            # Update webhook metadata
            webhook.last_sent = datetime.utcnow()
            webhook.retry_count = 0
            
            return {
                'status': 'success', 
                'code': response.status_code,
                'message': response.text
            }
        
        except requests.exceptions.RequestException as e:
            # Handle retry logic
            webhook.retry_count += 1
            
            if webhook.retry_count <= webhook.max_retries:
                self.logger.warning(f"Webhook send failed. Retry {webhook.retry_count}")
                return self.send_webhook(webhook, payload)
            
            self.logger.error(f"Webhook send failed after {webhook.max_retries} retries: {e}")
            return {
                'status': 'error', 
                'message': str(e)
            }

    def bulk_send(self, webhooks: list[Webhook], payload: Dict[str, Any]) -> list[Dict[str, Any]]:
        """
        Send payload to multiple webhooks
        
        Args:
            webhooks (list): List of webhooks
            payload (dict): Payload to send
        
        Returns:
            list: Results of webhook sends
        """
        import concurrent.futures
        
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(self.send_webhook, webhook, payload): webhook 
                for webhook in webhooks
            }
            
            for future in concurrent.futures.as_completed(futures):
                webhook = futures[future]
                try:
                    result = future.result()
                    results.append({
                        'webhook_id': webhook.id,
                        'webhook_type': webhook.type.name,
                        **result
                    })
                except Exception as e:
                    results.append({
                        'webhook_id': webhook.id,
                        'status': 'error',
                        'message': str(e)
                    })
        
        return results

# Example usage
if __name__ == "__main__":
    # Create webhook
    email_webhook = Webhook(
        name="Email Notification Webhook",
        url="https://example.com/webhook",
        type=WebhookType.EMAIL_NOTIFICATION,
        secret_key="your_secret_key"
    )

    # Create dispatcher
    dispatcher = WebhookDispatcher()

    # Sample payload
    payload = {
        'event': 'user_registered',
        'user_id': '12345',
        'email': 'user@example.com'
    }

    # Send webhook
    result = dispatcher.send_webhook(email_webhook, payload)
    print("Webhook Send Result:", result)