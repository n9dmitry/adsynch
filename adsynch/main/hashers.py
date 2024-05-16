import base64
import hashlib
from django.contrib.auth.hashers import BasePasswordHasher

class Base64PasswordHasher(BasePasswordHasher):
    algorithm = "base64"

    def encode(self, password, salt):
        assert password is not None
        return base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest()).decode('utf-8')

    def verify(self, password, encoded):
        return encoded == self.encode(password, '')

    def safe_summary(self, encoded):
        return {
            'algorithm': self.algorithm,
        }