
import re
from typing import Dict, Any

def validate_email(email: str) -> bool:
    """
    Validate email address format
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def format_email(email: Dict[str, Any]) -> str:
    """
    Format email into a readable string
    
    Args:
        email (dict): Email details
    
    Returns:
        str: Formatted email string
    """
    return f"""
To: {email.get('to', 'N/A')}
Subject: {email.get('subject', 'No Subject')}

{email.get('body', '')}
"""

def sanitize_email_address(email: str) -> str:
    """
    Sanitize and normalize email address
    
    Args:
        email (str): Email address to sanitize
    
    Returns:
        str: Sanitized email address
    """
    # Remove leading/trailing whitespace
    email = email.strip()
    
    # Convert to lowercase
    email = email.lower()
    
    return email
