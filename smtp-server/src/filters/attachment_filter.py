class AttachmentFilter:
    @staticmethod
    def check_attachments(email: dict) -> bool:
        """
        Check for potentially harmful attachments
        
        Args:
            email (dict): Email details dictionary
        
        Returns:
            bool: True if attachments are safe, False otherwise
        """
        allowed_extensions = ['.pdf', '.docx', '.txt']
        attachments = email.get('attachments', [])
        
        for attachment in attachments:
            if not any(attachment.endswith(ext) for ext in allowed_extensions):
                return False
        
        return True
