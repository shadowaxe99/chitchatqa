```python
from cryptography.fernet import Fernet
import os

class DataSecurity:

    def __init__(self):
        self.key = self.generate_key()
        self.cipher_suite = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_data(self, data):
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt_data(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def store_key(self):
        with open("secret.key", "wb") as key_file:
            key_file.write(self.key)

    def load_key(self):
        return open("secret.key", "rb").read()

    def secure_data(self, data):
        encrypted_data = self.encrypt_data(data)
        self.store_key()
        return encrypted_data

    def retrieve_data(self, encrypted_data):
        self.key = self.load_key()
        self.cipher_suite = Fernet(self.key)
        return self.decrypt_data(encrypted_data)
```