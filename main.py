# import section
import time
from MyEncryptRSA import encrypt_data, generate_key_pair_rsa
from MyDecryptRSA import decrypt_data_rsa
from MyEncryptECC import generate_key_pair_ecc, generate_shared_key_ecc, encrypt_data_ecc
from MyDecryptECC import decrypt_data_ecc

# Pip section
# pip install cryptography

# Start
if __name__ == '__main__':
    print('Welcome to my first Python application. '
          'The main purpose of this application is to test and illustrate difference in speed with Encryption and '
          'Decryption of RSA and ECC')
    print('________________________________________________________________________________')
    print('Generating RSA Encryption File')

# Generate RSA key pair and save the public key
    generate_key_pair_rsa()

    print(f'Going to call the RSA encrypt function now')


# Continue with encryption and decryption RSA
public_key_file_RSA = 'public_key_RSA.pem'
private_key_file_RSA = 'private_key_RSA.pem'

# RSA Encrypt data

# plaintext = input("Enter the plaintext to encrypt :")
plaintext = ('Speed of encryption and decryption measurement for RSA and ECC. '
             'Why dont we use more of the one versus the other if it is so much faster')

start_time_RSA = time.time()
ciphertext_RSA = encrypt_data(plaintext, public_key_file_RSA)
end_time_RSA = time.time()
encryption_time_RSA = end_time_RSA - start_time_RSA
print('RSA Ciphertext:', ciphertext_RSA)

# Decrypt RSA data
start_time_RSA = time.time()
decrypted_text = decrypt_data_rsa(ciphertext_RSA, private_key_file_RSA)
end_time_RSA = time.time()
decryption_time_RSA = end_time_RSA - start_time_RSA
print('RSA Decrypted text:', decrypted_text)
print('RSA Encryption Time:', encryption_time_RSA)
print('RSA Description Time:', decryption_time_RSA)
print('________________________________________________________________________________')

# ECC Encrypt
print('Generating ECC Encryption File')
generate_key_pair_ecc()

# Continue with ECC encryption and decryption
public_key_file_ECC = 'public_key_ECC.pem'
private_key_file_ECC = 'private_key_ECC.pem'

# Encrypt data and measure the performance
shared_Key_ECC = generate_shared_key_ecc(private_key_file_ECC, public_key_file_ECC)
start_time_ECC = time.time()
ciphertext_ECC = encrypt_data_ecc(plaintext, shared_Key_ECC)
end_time_ECC = time.time()
encryption_time_ECC = end_time_ECC - start_time_ECC
print('Ciphertext ECC:', ciphertext_ECC)


# Decrypt data and measure the performance
start_time_ECC = time.time()
decrypted_text_ECC = decrypt_data_ecc(ciphertext_ECC, private_key_file_ECC, public_key_file_ECC)
end_time_ECC = time.time()
decryption_time_ECC = end_time_ECC - start_time_ECC

print('ECC Decrypted text:', decrypted_text_ECC)
print('ECC Encryption Time:', encryption_time_ECC)
print('ECC Decrypted Time:', decryption_time_ECC)
print('________________________________________________________________________________')
# print('ECC is % faster than RSA with encoding:',encryption_time_RSA * 100 "/ " encryption_time_ECC *100)


if encryption_time_RSA != 0.0:
    percentage_time_encryption = (encryption_time_RSA - encryption_time_ECC) / encryption_time_RSA * 100
    print(f"The Percentage time for encryption difference is: {percentage_time_encryption:.2f}%")
    if encryption_time_RSA < encryption_time_ECC:
        print('RSA is the clear winner with encryption')
    else:
        print('ECC is the clear winner with encryption')
else:
    print('Error: Cannot calculate percentage time for encryption. Division by zero.')

if decryption_time_RSA != 0.0:
    percentage_time_decryption = (decryption_time_RSA - decryption_time_ECC) / decryption_time_RSA * 100
    print(f"The Percentage time for decryption difference is: {percentage_time_decryption:.2f}%")
    if decryption_time_RSA < decryption_time_ECC:
        print('RSA is the clear winner with decryption')
    else:
        print('ECC is the clear winner with decryption')
else:
    print('Error: Cannot calculate percentage time for decryption. Division by zero.')
