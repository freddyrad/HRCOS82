# import section
import os
import time
import psutil
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


# test memory, this is working better
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memory_use_start_rsa = python_process.memory_info()[0] / 2. ** 30
    print('memory use Start:', memory_use_start_rsa)
# New CPU Measure
    initial_rsa_cpu_time = psutil.cpu_times()
# Set Memory
    memory_info = psutil.virtual_memory()
    initial_memory_usage_keygen_rsa = memory_info.used
# Generate RSA key pair and save the public key
    generate_key_pair_rsa()

# Set memory
    final_memory_usage_keygen_rsa = memory_info.used
    memory_usage_diff_keygen_rsa = final_memory_usage_keygen_rsa - initial_memory_usage_keygen_rsa
    print(f'Going to call the RSA encrypt function now')
# Continue with encryption and decryption RSA
    public_key_file_RSA = 'public_key_RSA.pem'
    private_key_file_RSA = 'private_key_RSA.pem'
# plaintext = input("Enter the plaintext to encrypt :")
    plaintext = ('Speed of encryption and decryption measurement for RSA and ECC. '
                 'Why dont we use more of the one versus the other if it is so much faster')

    start_time_RSA = time.time()

# Set Memory counter
    memory_info = psutil.virtual_memory()
    initial_memory_usage_encrypt_rsa = memory_info.used

# RSA Encrypt data
    ciphertext_RSA = encrypt_data(plaintext, public_key_file_RSA)
    end_time_RSA = time.time()
    encryption_time_RSA = end_time_RSA - start_time_RSA

# Set Memory counter
    final_memory_usage_encrypt_rsa = memory_info.used
    memory_usage_diff_encrypt_rsa = final_memory_usage_encrypt_rsa - initial_memory_usage_encrypt_rsa
    print('RSA Ciphertext:', ciphertext_RSA)

# Decrypt RSA data
    start_time_RSA = time.time()
    decrypted_text = decrypt_data_rsa(ciphertext_RSA, private_key_file_RSA)
    end_time_RSA = time.time()
    decryption_time_RSA = end_time_RSA - start_time_RSA
    memory_use_end_rsa = python_process.memory_info()[0] / 2. ** 30
    memory_used_rsa = memory_use_end_rsa - memory_use_start_rsa

    print('Memory Used RSA:', memory_used_rsa)
    print('RSA Decrypted text:', decrypted_text)
    print('RSA Encryption Time:', encryption_time_RSA)
    print('RSA Decryption Time:', decryption_time_RSA)

    final_rsa_cpu_time = psutil.cpu_times()
    cpu_usage_rsa = psutil.cpu_percent(interval=None, percpu=False)
    print(f"Initial RSA CPU Time: {initial_rsa_cpu_time}")
    print(f"Final RSA CPU time: {final_rsa_cpu_time}")
    print(f"RSA CPU usage: {cpu_usage_rsa}%")
    print('________________________________________________________________________________')
# ECC Encrypt
    print('Generating ECC Encryption File')
# Get Memory details
    memory_use_start_ecc = python_process.memory_info()[0] / 2. ** 30

# Measure CPU
    initial_ecc_cpu_time = psutil.cpu_times()

# Generate the ECC KeyPair
    generate_key_pair_ecc()

# Continue with ECC encryption and decryption
    public_key_file_ECC = 'public_key_ECC.pem'
    private_key_file_ECC = 'private_key_ECC.pem'
# Encrypt data and measure the performance
    start_time_ECC = time.time()
    shared_Key_ECC = generate_shared_key_ecc(private_key_file_ECC, public_key_file_ECC)
    ciphertext_ECC = encrypt_data_ecc(plaintext, shared_Key_ECC)

    end_time_ECC = time.time()
    encryption_time_ECC = end_time_ECC - start_time_ECC
    print('Ciphertext ECC:', ciphertext_ECC)
# Decrypt data and measure the performance
    start_time_ECC = time.time()
    decrypted_text_ECC = decrypt_data_ecc(ciphertext_ECC, private_key_file_ECC, public_key_file_ECC)
    end_time_ECC = time.time()
    decryption_time_ECC = end_time_ECC - start_time_ECC
# Get Memory details
    memory_use_end_ecc = python_process.memory_info()[0] / 2. ** 30
    memory_used_ecc = memory_use_end_ecc - memory_use_start_ecc

    print('Memory Used ECC:', memory_used_ecc)
    print('ECC Decrypted text:', decrypted_text_ECC)
    print('ECC Encryption Time:', encryption_time_ECC)
    print('ECC Decrypted Time:', decryption_time_ECC)

    final_ecc_cpu_time = psutil.cpu_times()
    cpu_usage_ecc = psutil.cpu_percent(interval=None, percpu=False)
    print(f"Initial ECC CPU Time: {initial_ecc_cpu_time}")
    print(f"Final ECC CPU time: {final_ecc_cpu_time}")
    print(f"ECC CPU usage: {cpu_usage_ecc}%")

    print('________________________________________________________________________________')

    if encryption_time_RSA != 0.0:
        percentage_time_encryption = abs((encryption_time_RSA - encryption_time_ECC) / encryption_time_RSA * 100)
        print(f"The Percentage time for encryption difference is: {percentage_time_encryption:.2f}%")
        if encryption_time_RSA < encryption_time_ECC:
            print('RSA is the clear winner with encryption')
        else:
            print('ECC is the clear winner with encryption')
    else:
        print('Error: Cannot calculate percentage time for encryption. Division by zero.')

    if decryption_time_RSA != 0.0:
        percentage_time_decryption = abs((decryption_time_RSA - decryption_time_ECC) / decryption_time_RSA * 100)
        print(f"The Percentage time for decryption difference is: {percentage_time_decryption:.2f}%")
        if decryption_time_RSA < decryption_time_ECC:
            print('RSA is the clear winner with decryption')
        else:
            print('ECC is the clear winner with decryption')
    else:
        print('Error: Cannot calculate percentage time for decryption. Division by zero.')

    if memory_used_rsa > memory_used_ecc:
        print('RSA used more memory than ECC by:', memory_used_rsa - memory_used_ecc)
    else:
        print('ECC used more memory than RSA by:', memory_used_ecc - memory_used_rsa)
    memory_diff = abs((memory_used_ecc - memory_used_rsa) / memory_used_rsa * 100)
    print(f"Percentage memory difference: {memory_diff}%")