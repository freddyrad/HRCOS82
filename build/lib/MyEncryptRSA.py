# import section
# pip install cryptography
# pip install rsa
# pip install pycryptodome

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os


def generate_key_pair_rsa():
    # Generate an RSA key pair
    private_key_rsa = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Serialize the private key to PEM format
    pem_private_key = private_key_rsa.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open("private_key_rsa.pem", "wb") as f:
        f.write(pem_private_key)

    # Extract the public key from the private key
    public_key_rsa = private_key_rsa.public_key()

    # Serialize the public key to PEM format
    pem_public_key_rsa = public_key_rsa.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the public key to a file
    with open("public_key_rsa.pem", 'wb') as f:
        f.write(pem_public_key_rsa)

    print("RSA key pair generated and saved.")

def encrypt_data(data, public_key_file):
    # Load the public key from file
    with open(public_key_file, 'rb') as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Encrypt the data using the public key
    ciphertext = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext