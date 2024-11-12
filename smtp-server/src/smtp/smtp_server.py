
import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP as SMTPProtocol

class SMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        # Process incoming email
        print(f"Received email from: {envelope.mail_from}")
        print(f"Email recipients: {envelope.rcpt_tos}")
        return '250 Message accepted for delivery'

class SMTPServer:
    def __init__(self, host='0.0.0.0', port=25):
        self.handler = SMTPHandler()
        self.controller = Controller(self.handler, hostname=host, port=port)

    def start(self):
        self.controller.start()
        print(f"SMTP Server started on {self.controller.hostname}:{self.controller.port}")

    def stop(self):
        self.controller.stop()
