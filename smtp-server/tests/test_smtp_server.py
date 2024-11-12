import unittest
from notifications.email_notification import EmailQueue, EmailMessage, EmailPriority

class TestSMTPServer(unittest.TestCase):
    def setUp(self):
        # Setup method that runs before each test
        self.email_queue = EmailQueue()

    def test_email_queue_creation(self):
        # Basic test to check if EmailQueue can be created
        self.assertIsNotNone(self.email_queue)

    def test_add_email(self):
        # Test adding an email to the queue
        email = EmailMessage(
            to="test@example.com",
            subject="Test Subject",
            body="Test Body",
            priority=EmailPriority.NORMAL
        )
        self.email_queue.add(email)
        self.assertEqual(len(self.email_queue), 1)

    def test_send_emails(self):
        # Test sending emails (you might want to mock the actual sending)
        email1 = EmailMessage(
            to="test1@example.com",
            subject="Test Subject 1",
            body="Test Body 1",
            priority=EmailPriority.NORMAL
        )
        email2 = EmailMessage(
            to="test2@example.com",
            subject="Test Subject 2",
            body="Test Body 2",
            priority=EmailPriority.HIGH
        )
        
        self.email_queue.add(email1)
        self.email_queue.add(email2)
        
        # You might want to add a method to check if emails are sent
        # This is a placeholder - you'll need to implement the actual sending logic
        result = self.email_queue.send()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()