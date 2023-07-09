from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

import os

from MyDecryptECC import generate_shared_key


def generate_key_pair_ecc():
    # Generate an ECC key pair
    private_key_ecc = ec.generate_private_key(ec.SECP256R1())

    # Serialize the private key to PEM format
    pem_private_key = private_key_ecc.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Save the private key to a file
    with open('private_key_ecc.pem', 'wb') as f:
        f.write(pem_private_key)

    # Extract the public key from the private key
    public_key_ecc = private_key_ecc.public_key()

    # Serialize the public key to PEM format
    pem_public_key_ecc = public_key_ecc.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the public key to a file
    with open('public_key_ecc.pem', 'wb') as f:
        f.write(pem_public_key_ecc)

    print("ECC key pair generated and saved.")


def generate_shared_key_ecc(private_key_file, public_key_file):
    # Load the private key from file
    with open(private_key_file, 'rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )
        f.close()

    # Load the public key from file
    with open(public_key_file, 'rb') as f:
        public_key = serialization.load_pem_public_key(f.read())
        f.close()

    # Generate the shared key using the private key and public key
    shared_key = generate_shared_key(private_key, public_key)

    return shared_key


def encrypt_data_ecc(data, shared_key, encoding='utf-8'):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create an AES cipher with CBC mode
    cipher = Cipher(algorithms.AES(shared_key), modes.CBC(iv))

    # Create an encryptor object
    encryptor = cipher.encryptor()

    # Encode the data to the specified encoding
    encoded_data = data.encode(encoding)

    # Apply PKCS7 padding to the data
    padder = PKCS7(algorithms.AES.block_size * 8).padder()
    padded_data = padder.update(encoded_data) + padder.finalize()

    # Perform the encryption
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv + ciphertext
