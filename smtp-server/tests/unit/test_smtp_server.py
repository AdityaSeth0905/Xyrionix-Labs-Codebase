
import pytest
from src.smtp.smtp_server import SMTPServer, SMTPHandler

def test_smtp_server_initialization():
    server = SMTPServer()
    assert server is not None
    assert server.controller.hostname == '0.0.0.0'
    assert server.controller.port == 25

def test_smtp_handler():
    handler = SMTPHandler()
    # Add more specific tests for SMTPHandler
