import unittest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
from queue import Queue
import pytest
import notifications
from notifications.email_notification import EmailQueue, EmailMessage, EmailPriority

class TestEmailQueue(unittest.TestCase):
    def setUp(self):
        """
        Set up test environment before each test method
        """
        self.email_queue = EmailQueue()

    def test_create_email_message(self):
        """
        Test creating an email message
        """
        message = EmailMessage(
            sender='sender@example.com',
            recipient='recipient@example.com',
            subject='Test Subject',
            body='Test Body',
            priority=EmailPriority.MEDIUM
        )

        self.assertIsNotNone(message.id)
        self.assertEqual(message.sender, 'sender@example.com')
        self.assertEqual(message.recipient, 'recipient@example.com')
        self.assertEqual(message.subject, 'Test Subject')
        self.assertEqual(message.body, 'Test Body')
        self.assertEqual(message.priority, EmailPriority.MEDIUM)
        self.assertIsNotNone(message.timestamp)

    def test_email_queue_enqueue(self):
        """
        Test enqueuing email messages
        """
        message1 = EmailMessage(
            sender='sender1@example.com',
            recipient='recipient1@example.com',
            subject='Subject 1',
            body='Body 1',
            priority=EmailPriority.HIGH
        )

        message2 = EmailMessage(
            sender='sender2@example.com',
            recipient='recipient2@example.com',
            subject='Subject 2',
            body='Body 2',
            priority=EmailPriority.LOW
        )

        self.email_queue.enqueue(message1)
        self.email_queue.enqueue(message2)

        self.assertEqual(self.email_queue.size(), 2)

    def test_email_queue_dequeue(self):
        """
        Test dequeuing email messages with priority
        """
        high_priority = EmailMessage(
            sender='high@example.com',
            recipient='high_recipient@example.com',
            subject='High Priority',
            body='High Priority Body',
            priority=EmailPriority.HIGH
        )

        medium_priority = EmailMessage(
            sender='medium@example.com',
            recipient='medium_recipient@example.com',
            subject='Medium Priority',
            body='Medium Priority Body',
            priority=EmailPriority.MEDIUM
        )

        low_priority = EmailMessage(
            sender='low@example.com',
            recipient='low_recipient@example.com',
            subject='Low Priority',
            body='Low Priority Body',
            priority=EmailPriority.LOW
        )

        self.email_queue.enqueue(low_priority)
        self.email_queue.enqueue(high_priority)
        self.email_queue.enqueue(medium_priority)

        # Dequeue should return high priority first
        dequeued_message = self.email_queue.dequeue()
        self.assertEqual(dequeued_message.priority, EmailPriority.HIGH)
        self.assertEqual(dequeued_message.subject, 'High Priority')

    def test_email_queue_size(self):
        """
        Test email queue size tracking
        """
        self.assertEqual(self.email_queue.size(), 0)

        message1 = EmailMessage(
            sender='sender1@example.com',
            recipient='recipient1@example.com',
            subject='Subject 1',
            body='Body 1'
        )

        message2 = EmailMessage(
            sender='sender2@example.com',
            recipient='recipient2@example.com',
            subject='Subject 2',
            body='Body 2'
        )

        self.email_queue.enqueue(message1)
        self.email_queue.enqueue(message2)

        self.assertEqual(self.email_queue.size(), 2)

    def test_email_queue_is_empty(self):
        """
        Test checking if email queue is empty
        """
        self.assertTrue(self.email_queue.is_empty())

        message = EmailMessage(
            sender='sender@example.com',
            recipient='recipient@example.com',
            subject='Subject',
            body='Body'
        )

        self.email_queue.enqueue(message)
        self.assertFalse(self.email_queue.is_empty())

    @patch('notifications.email_queue.smtplib.SMTP')
    def test_email_sending(self, mock_smtp):
        """
        Test email sending functionality
        """
        # Configure mock SMTP
        mock_instance = mock_smtp.return_value
        mock_instance.send_message.return_value = {}

        message = EmailMessage(
            sender='sender@example.com',
            recipient='recipient@example.com',
            subject='Test Subject',
            body='Test Body'
        )

        # Simulate sending email
        result = self.email_queue.send_email(message)

        self.assertTrue(result)
        mock_instance.send_message.assert_called_once()

    def test_email_expiration(self):
        """
        Test email message expiration
        """
        old_message = EmailMessage(
            sender='old@example.com',
            recipient='old_recipient@example.com',
            subject='Old Message',
            body='Expired Message',
            timestamp=datetime.now() - timedelta(hours=25)  # Older than 24 hours
        )

        fresh_message = EmailMessage(
            sender='fresh@example.com',
            recipient='fresh_recipient@example.com',
            subject='Fresh Message',
            body='Fresh Message Body'
        )

        self.email_queue.enqueue(old_message)
        self.email_queue.enqueue(fresh_message)

        # Cleanup expired messages
        self.email_queue.cleanup_expired_messages()

        self.assertEqual(self.email_queue.size(), 1)
        remaining_message = self.email_queue.dequeue()
        self.assertEqual(remaining_message.subject, 'Fresh Message')

    @pytest.mark.parametrize('priority', [
        EmailPriority.LOW,
        EmailPriority.MEDIUM,
        EmailPriority.HIGH
    ])
    def test_email_priorities(self, priority):
        """
        Parameterized test for email priorities
        """
        message = EmailMessage(
            sender=f'{priority.name.lower()}@example.com',
            recipient=f'{priority.name.lower()}_recipient@example.com',
            subject=f'{priority.name} Priority Message',
            body=f'{priority.name} Priority Body',
            priority=priority
        )

        self.assertEqual(message.priority, priority)

def main():
    unittest.main()

if __name__ == '__main__':
    main()