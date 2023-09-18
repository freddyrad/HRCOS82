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
# Function for measuring cpu performance
def measure_cpu_usage():
    cpu_percentages = []
    for _ in range(1):  # Measure for 1 seconds
        cpu_percentages.append(psutil.cpu_percent(interval=1))

    avg_cpu_usage = max(0, int(sum(cpu_percentages) / len(cpu_percentages)))
    return avg_cpu_usage


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
# Measure CPU
    cpu_before_keygen_rsa = measure_cpu_usage()
# Set Memory
    memory_info = psutil.virtual_memory()
    initial_memory_usage_keygen_rsa = memory_info.used
# Generate RSA key pair and save the public key
    generate_key_pair_rsa()
# Measure CPU
    cpu_after_keygen_rsa = measure_cpu_usage()
    keygen_cpu_usage_rsa = cpu_after_keygen_rsa - cpu_before_keygen_rsa
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
# Measure CPU
    cpu_before_encrypt_rsa = measure_cpu_usage()
    start_time_RSA = time.time()

# Set Memory counter
    memory_info = psutil.virtual_memory()
    initial_memory_usage_encrypt_rsa = memory_info.used

# RSA Encrypt data
    ciphertext_RSA = encrypt_data(plaintext, public_key_file_RSA)
    end_time_RSA = time.time()
    encryption_time_RSA = end_time_RSA - start_time_RSA

# Measure CPU
    cpu_after_encrypt_rsa = measure_cpu_usage()
    encrypt_cpu_usage_rsa = cpu_after_encrypt_rsa - cpu_before_encrypt_rsa

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
# print('Memory use End:', memory_use_end_rsa)
    print('Memory Used RSA:', memory_used_rsa)

    print('RSA Decrypted text:', decrypted_text)
    print('RSA Encryption Time:', encryption_time_RSA)
    print('RSA Description Time:', decryption_time_RSA)
    print(f"CPU Usage for Key Pair Generation RSA: {keygen_cpu_usage_rsa}%")
    print(f"CPU Usage for Encryption RSA: {encrypt_cpu_usage_rsa}%")
# print('Memory Usage for Keygen RSA:', memory_usage_diff_keygen_rsa)
# print('Memory Usage for Encrypt RSA:', memory_usage_diff_encrypt_rsa)
    print('________________________________________________________________________________')
# ECC Encrypt
    print('Generating ECC Encryption File')
# Get Memory details
    memory_use_start_ecc = python_process.memory_info()[0] / 2. ** 30
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
# Get Memory details
    memory_use_end_ecc = python_process.memory_info()[0] / 2. ** 30
    memory_used_ecc = memory_use_end_ecc - memory_use_start_ecc
    print('Memory Used ECC:', memory_used_ecc)
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

    if memory_used_rsa > memory_used_ecc:
        print('RSA used more memory than ECC by:', memory_used_rsa - memory_used_ecc)
    else:
        print('ECC used more memory than RSA by:', memory_used_ecc - memory_used_rsa)
