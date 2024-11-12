
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class AsymmetricEncryption:
    @staticmethod
    def generate_key_pair():
        """Generate a new RSA key pair"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key
    
    @staticmethod
    def encrypt(message: str, public_key):
        """Encrypt a message using public key"""
        encrypted = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted
    
    @staticmethod
    def decrypt(encrypted_message: bytes, private_key):
        """Decrypt a message using private key"""
        decrypted = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()
