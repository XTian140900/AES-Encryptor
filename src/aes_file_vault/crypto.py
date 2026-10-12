
import os
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


# File format:
# MAGIC (8 bytes) + SALT (16 bytes) + NONCE (12 bytes) + CIPHERTEXT
MAGIC = b"AESVAULT"
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32  # 256-bit AES key


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 256-bit encryption key from a password."""
    if not password:
        raise ValueError("Password required.")

    kdf = Scrypt(
        salt=salt,
        length=KEY_SIZE,
        n=2**14,
        r=8,
        p=1,
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt bytes using AES-256-GCM."""
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    key = derive_key(password, salt)
    ciphertext = AESGCM(key).encrypt(nonce, data, MAGIC)

    return MAGIC + salt + nonce + ciphertext


def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    """Decrypt bytes and authenticate the encrypted data."""
    header_size = len(MAGIC) + SALT_SIZE + NONCE_SIZE

    if len(encrypted_data) < header_size + 16:
        raise ValueError("Encrypted file not valid.")

    if not encrypted_data.startswith(MAGIC):
        raise ValueError("Format unknown.")

    offset = len(MAGIC)
    salt = encrypted_data[offset:offset + SALT_SIZE]
    offset += SALT_SIZE

    nonce = encrypted_data[offset:offset + NONCE_SIZE]
    ciphertext = encrypted_data[header_size:]

    key = derive_key(password, salt)

    try:
        return AESGCM(key).decrypt(nonce, ciphertext, MAGIC)
    except InvalidTag as exc:
        raise ValueError(
            "Decryption failed : Password or data not match."
        ) from exc
