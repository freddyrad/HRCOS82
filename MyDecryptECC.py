from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7


def decrypt_data_ecc(ciphertext, private_key_file, public_key_file, encoding='utf-8'):
    # Load the private key from file
    with open(private_key_file, 'rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    # Load the public key from file
    with open(public_key_file, 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read()
        )

    # Extract the IV and ciphertext from the input
    iv = ciphertext[:16]
    encrypted_data = ciphertext[16:]

    # Generate the shared key using the private key and the public key
    shared_key = generate_shared_key(private_key, public_key)

    # Create an AES cipher with CBC mode
    cipher = Cipher(algorithms.AES(shared_key), modes.CBC(iv))

    # Create a decryptor object
    decryptor = cipher.decryptor()

    # Perform the decryption
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove PKCS7 padding from the decrypted data
    unpadder = PKCS7(algorithms.AES.block_size * 8).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Decode the decrypted data with the specified encoding
    decoded_data = unpadded_data.decode(encoding)

    return decoded_data


# def generate_shared_key_ECC(private_key):
#    shared_key = private_key.exchange(ec.ECDH())
#    return shared_key
def generate_shared_key(private_key, public_key):
    # Derive the shared secret using the private key and the public key
    shared_secret = private_key.exchange(ec.ECDH(), public_key)

    # Derive a symmetric key from the shared secret using HKDF
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'',
    ).derive(shared_secret)

    return derived_key
