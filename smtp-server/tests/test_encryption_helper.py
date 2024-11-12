# test/test_encryption_helper.py

import unittest
from utils.encryption_helper import EncryptionHelper

class TestEncryptionHelper(unittest.TestCase):
    def setUp(self):
        self.helper = EncryptionHelper()

    def test_encryption_decryption(self):
        original_text = "Test encryption"
        encrypted_text = self.helper.encrypt(original_text)
        decrypted_text = self.helper.decrypt(encrypted_text)
        self.assertEqual(original_text, decrypted_text)

    def test_encrypt_invalid_input(self):
        with self.assertRaises(ValueError):
            self.helper.encrypt(12345)  # Should raise an error

    def test_decrypt_invalid_input(self):
        with self.assertRaises(ValueError):
            self.helper.decrypt(12345)  # Should raise an error

    def test_save_and_load_key(self):
        key_file_path = 'test_key.key'
        self.helper.save_key(key_file_path)
        loaded_key = EncryptionHelper.load_key(key_file_path)
        self.assertEqual(self.helper.get_key(), loaded_key)

if __name__ == '__main__':
    unittest.main()