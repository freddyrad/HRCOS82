from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def decrypt_data_rsa(ciphertext, private_key_file_rsa):
    # Load the private key from file
    with open(private_key_file_rsa, 'rb') as f:
        private_key_rsa = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    # Decrypt the ciphertext using the private key
    plaintext = private_key_rsa.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()
