# utils/encryption_helper.py

from cryptography.fernet import Fernet
import base64
import os

class EncryptionHelper:
    def __init__(self):
        # Generate a key for encryption and decryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext: str) -> str:
        """Encrypts a plaintext string."""
        if isinstance(plaintext, str):
            plaintext_bytes = plaintext.encode('utf-8')
            encrypted_bytes = self.cipher.encrypt(plaintext_bytes)
            return encrypted_bytes.decode('utf-8')
        else:
            raise ValueError("Input must be a string")

    def decrypt(self, encrypted_text: str) -> str:
        """Decrypts an encrypted string."""
        if isinstance(encrypted_text, str):
            encrypted_bytes = encrypted_text.encode('utf-8')
            decrypted_bytes = self.cipher.decrypt(encrypted_bytes)
            return decrypted_bytes.decode('utf-8')
        else:
            raise ValueError("Input must be a string")

    def get_key(self) -> bytes:
        """Returns the encryption key."""
        return self.key

    def save_key(self, file_path: str):
        """Saves the encryption key to a file."""
        with open(file_path, 'wb') as key_file:
            key_file.write(self.key)

    @staticmethod
    def load_key(file_path: str) -> bytes:
        """Loads the encryption key from a file."""
        return open(file_path, 'rb').read()