
from cryptography.fernet import Fernet
import base64
import os

class SymmetricEncryption:
    @staticmethod
    def generate_key():
        """Generate a new encryption key"""
        return Fernet.generate_key()
    
    @staticmethod
    def encrypt(message: str, key: bytes) -> bytes:
        """Encrypt a message"""
        f = Fernet(key)
        return f.encrypt(message.encode())
    
    @staticmethod
    def decrypt(encrypted_message: bytes, key: bytes) -> str:
        """Decrypt a message"""
        f = Fernet(key)
        return f.decrypt(encrypted_message).decode()
