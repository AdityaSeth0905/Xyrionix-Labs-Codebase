
class EmailQueueError(Exception):
    """Base exception for email queue errors"""
    pass

class QueueFullError(EmailQueueError):
    """Raised when email queue is full"""
    pass

class EmailSendError(EmailQueueError):
    """Raised when email sending fails"""
    pass
