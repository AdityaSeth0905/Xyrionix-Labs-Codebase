import re
import html
from typing import Dict, Optional

class ContentFilter:
    @staticmethod
    def sanitize_html(text: Optional[str], allow_basic_formatting: bool = True) -> str:
        """
        Comprehensive HTML sanitization function
        
        Args:
            text (str): Input text to sanitize
            allow_basic_formatting (bool): Allow safe HTML formatting tags
        
        Returns:
            str: Sanitized HTML text
        """
        # Handle None or empty input
        if not text:
            return ""
        
        # HTML escape to prevent XSS
        text = html.escape(text)
        
        # If only basic escaping is needed
        if not allow_basic_formatting:
            return text
        
        # Whitelist of allowed safe HTML tags
        allowed_tags = [
            'b', 'i', 'u', 'strong', 'em', 'br', 
            'p', 'div', 'span', 'ul', 'ol', 'li', 
            'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
        ]
        
        # Remove script tags and event handlers
        text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'\s(on\w+)=([\'"])[^\'"]*(\2)', '', text, flags=re.IGNORECASE)
        
        # Remove potentially dangerous attributes
        dangerous_attrs = [
            'javascript:', 'vbscript:', 'data:', 
            'src=', 'href=', 'background='
        ]
        for attr in dangerous_attrs:
            text = text.replace(attr, '')
        
        # Reconstruct safe tags
        def sanitize_tag(match):
            tag = match.group(1).lower()
            content = match.group(2)
            
            # Check if tag is in allowed list
            if tag in allowed_tags:
                # Additional checks for specific tags
                if tag == 'a':
                    # Ensure href is safe
                    content = re.sub(r'href=[\'"]?([^\'" >]+)', 
                                     lambda m: f'href="{html.escape(m.group(1))}"' 
                                     if m.group(1).startswith(('http://', 'https://')) 
                                     else '', 
                                     content)
                
                return f'<{tag}>{content}</{tag}>'
            return content
        
        # Replace tags while preserving content
        text = re.sub(r'<(\w+)>(.*?)</\1>', sanitize_tag, text, flags=re.DOTALL)
        
        return text

    @staticmethod
    def sanitize_email(email: Dict[str, str]) -> Dict[str, str]:
        """
        Sanitize email content to remove potentially harmful content
        
        Args:
            email (dict): Original email dictionary
        
        Returns:
            dict: Sanitized email dictionary
        """
        # Sanitize subject and body
        sanitized_email = email.copy()
        sanitized_email['subject'] = ContentFilter.sanitize_html(email.get('subject', ''))
        sanitized_email['body'] = ContentFilter.sanitize_html(email.get('body', ''))
        
        return sanitized_email

# Example usage
if __name__ == "__main__":
    # Test cases
    test_emails = [
        {
            'subject': 'Hello <script>alert("XSS")</script>',
            'body': 'Click <a href="javascript:alert(\'Hacked\')">here</a>'
        },
        {
            'subject': 'Safe Email',
            'body': 'Some <b>bold</b> and <a href="https://example.com">link</a> content'
        }
    ]
    
    for email in test_emails:
        print("Original:")
        print(email)
        print("\nSanitized:")
        print(ContentFilter.sanitize_email(email))
        print("\n---\n")