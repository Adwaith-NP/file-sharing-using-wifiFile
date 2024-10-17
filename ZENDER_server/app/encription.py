from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

# Function to generate a key from a password
def generate_key(password: str, salt: bytes) -> bytes:
    # Derive a key using PBKDF2 HMAC with SHA256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Fernet requires a 32-byte key
        salt=salt,
        iterations=100000,  # Number of iterations for key derivation
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Function to encrypt a message
def encrypt_message(password: str, message: str) -> str:
    # Generate a salt for the key derivation
    salt = os.urandom(16)  # Generate a random salt
    key = generate_key(password, salt)  # Derive the key from the password
    fernet = Fernet(key)  # Create a Fernet object

    encrypted_message = fernet.encrypt(message.encode())  # Encrypt the message
    # Combine salt and encrypted message for decryption
    return base64.urlsafe_b64encode(salt + encrypted_message).decode()

# Function to decrypt a message
def decrypt_message(password: str, encrypted_message: str) -> str:
    # Decode the combined salt and encrypted message
    decoded_data = base64.urlsafe_b64decode(encrypted_message.encode())
    salt = decoded_data[:16]  # Extract the salt
    encrypted_message = decoded_data[16:]  # Extract the encrypted message

    key = generate_key(password, salt)  # Derive the key using the same salt
    fernet = Fernet(key)  # Create a Fernet object

    # Decrypt the message
    return fernet.decrypt(encrypted_message).decode()

# Example usage
if __name__ == "__main__":
    password = "my_strong_password"
    original_message = "This is a secret message."

    # Encrypt the message
    encrypted = encrypt_message(password, original_message)
    print(f"Encrypted Message: {encrypted}")

    # Decrypt the message
    decrypted = decrypt_message(password, encrypted)
    print(f"Decrypted Message: {decrypted}")
