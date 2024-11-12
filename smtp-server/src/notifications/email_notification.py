import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from typing import Optional, Dict, Any
import uuid
from datetime import datetime, timedelta
from enum import Enum, auto

class EmailPriority(Enum):
    """
    Enumeration of email priorities
    """
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class EmailMessage:
    """
    Represents an email message with all necessary details
    """
    def __init__(
        self, 
        sender: str, 
        recipient: str, 
        subject: str, 
        body: str, 
        priority: EmailPriority = EmailPriority.MEDIUM,
        timestamp: Optional[datetime] = None
    ):
        """
        Initialize an email message
        
        Args:
            sender (str): Sender's email address
            recipient (str): Recipient's email address
            subject (str): Email subject
            body (str): Email body
            priority (EmailPriority, optional): Email priority
            timestamp (datetime, optional): Message creation timestamp
        """
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.priority = priority
        self.timestamp = timestamp or datetime.now()
        self.attempts = 0

class EmailQueue:
    """
    Manages a queue of email messages with priority and sending capabilities
    """
    def __init__(self, max_retries: int = 3, expiration_hours: int = 24):
        """
        Initialize the email queue
        
        Args:
            max_retries (int, optional): Maximum number of send attempts
            expiration_hours (int, optional): Hours after which message expires
        """
        self._queue = []
        self._max_retries = max_retries
        self._expiration_hours = expiration_hours
        self._logger = logging.getLogger(__name__)

    def enqueue(self, message: EmailMessage):
        """
        Add a message to the queue
        
        Args:
            message (EmailMessage): Message to enqueue
        """
        self._queue.append(message)
        # Sort queue by priority (high to low)
        self._queue.sort(key=lambda x: x.priority.value, reverse=True)

    def dequeue(self) -> Optional[EmailMessage]:
        """
        Remove and return the highest priority message
        
        Returns:
            Optional[EmailMessage]: Highest priority message or None
        """
        return self._queue.pop(0) if self._queue else None

    def size(self) -> int:
        """
        Get the current queue size
        
        Returns:
            int: Number of messages in the queue
        """
        return len(self._queue)

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return len(self._queue) == 0

    def cleanup_expired_messages(self):
        """
        Remove messages older than expiration time
        """
        current_time = datetime.now()
        self._queue = [
            msg for msg in self._queue 
            if (current_time - msg.timestamp).total_seconds() / 3600 <= self._expiration_hours
        ]

    def send_email(self, message: EmailMessage) -> bool:
        """
        Send an email message
        
        Args:
            message (EmailMessage): Message to send
        
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Create MIME message
            mime_message = MIMEMultipart()
            mime_message['From'] = message.sender
            mime_message['To'] = message.recipient
            mime_message['Subject'] = message.subject
            
            # Attach body
            mime_message.attach(MIMEText(message.body, 'plain'))
            
            # Send email using SMTP
            with smtplib.SMTP('localhost', 25) as server:
                server.send_message(mime_message)
            
            return True
        except Exception as e:
            self._logger.error(f"Failed to send email: {e}")
            message.attempts += 1
            return False

class EmailNotification:
    """
    Handles email notification sending
    """
    @staticmethod
    def send_notification(
        email: str, 
        subject: str, 
        message: str, 
        sender: Optional[str] = 'notifications@example.com',
        priority: EmailPriority = EmailPriority.MEDIUM
    ):
        """
        Send an email notification
        
        Args:
            email (str): Recipient email address
            subject (str): Email subject
            message (str): Email body
            sender (str, optional): Sender email address
            priority (EmailPriority, optional): Email priority
        """
        email_message = EmailMessage(
            sender=sender,
            recipient=email,
            subject=subject,
            body=message,
            priority=priority
        )
        
        email_queue = EmailQueue()
        email_queue.enqueue(email_message)
        
        # Attempt to send immediately
        email_queue.send_email(email_message)

