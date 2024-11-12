
import re
from typing import Dict, Any

class SpamFilter:
    @staticmethod
    def check_spam(email: Dict[str, Any]) -> bool:
        """
        Basic spam detection logic
        
        Args:
            email (Dict): Email details dictionary
        
        Returns:
            bool: True if email is spam, False otherwise
        """
        spam_keywords = [
            'viagra', 'cialis', 'lottery', 'winner', 
            'inheritance', 'prince', 'urgent'
        ]
        
        # Check subject and body for spam keywords
        subject = email.get('subject', '').lower()
        body = email.get('body', '').lower()
        
        # Keyword-based spam detection
        for keyword in spam_keywords:
            if keyword in subject or keyword in body:
                return True
        
        # Check for excessive links
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
        if len(links) > 5:
            return True
        
        return False
