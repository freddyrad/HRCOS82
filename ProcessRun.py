import os
import time
import psutil
from MyEncryptRSA import encrypt_data, generate_key_pair_rsa
from MyDecryptRSA import decrypt_data_rsa
from MyEncryptECC import generate_key_pair_ecc, generate_shared_key_ecc, encrypt_data_ecc
from MyDecryptECC import decrypt_data_ecc


def memory_usage(stat):

    memory = psutil.virtual_memory()
    memory_stats = {
        "total_memory": memory.total,
        "available_memory": memory.available,
        "used_memory": memory.used,
        "free_memory": memory.free
    }
    if stat in memory_stats:
        return memory_stats[stat]
    else:
        return f"Invalid memory stat {stat} requested"


def execute(process_size):
    if process_size == 'Small':
        print('Small')
    if process_size == 'Medium':
        print('Medium')
    if process_size == 'Large':
        print('Large')

# test memory, this is working better
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memory_use_start_rsa = python_process.memory_info()[0] / 2. ** 30
#   30 for GB memory use 10 for kilobytes
    print('memory use Start:', memory_use_start_rsa)
# New CPU Measure
    initial_rsa_cpu_time = psutil.cpu_times()
# Set Memory
#    memory_info = psutil.virtual_memory()
#    initial_memory_usage_keygen_rsa = memory_info.used
# Generate RSA key pair and save the public key
    generate_key_pair_rsa()

# Set memory
#    final_memory_usage_keygen_rsa = memory_info.used
#    memory_usage_diff_keygen_rsa = final_memory_usage_keygen_rsa - initial_memory_usage_keygen_rsa
    print(f'Going to call the RSA encrypt function now')
# Continue with encryption and decryption RSA
    public_key_file_rsa = 'public_key_RSA.pem'
    private_key_file_rsa = 'private_key_RSA.pem'

    if process_size == 'Small':
        plaintext = (
            'Speed of encryption and decryption measurement for RSA and ECC.')

    if process_size == 'Medium':
        plaintext = (
            'Speed of encryption and decryption measurement for RSA and ECC.'
            'Why dont we use more of the one versus the other if it is so much faster.')

    if process_size == 'Large':
        plaintext = (
            'Speed of encryption and decryption measurement for RSA and ECC. '
            'Why dont we use more of the one versus the other if it is so much faster'
            'The input size has been increased for the comparison.')

    sizeofinput = len(plaintext)
    print("The size of input is:", sizeofinput)

    start_time_rsa = time.time()

# Set Memory counter
#    memory_info = psutil.virtual_memory()
#    initial_memory_usage_encrypt_rsa = memory_info.used

#   RSA Encrypt data
    ciphertext_rsa = encrypt_data(plaintext, public_key_file_rsa)
    end_time_rsa = time.time()
    encryption_time_rsa = end_time_rsa - start_time_rsa

# Set Memory counter
#    final_memory_usage_encrypt_rsa = memory_info.used
#    memory_usage_diff_encrypt_rsa = final_memory_usage_encrypt_rsa - initial_memory_usage_encrypt_rsa
    print('RSA Ciphertext:', ciphertext_rsa)

# Decrypt RSA data
    start_time_rsa = time.time()
    decrypted_text = decrypt_data_rsa(ciphertext_rsa, private_key_file_rsa)
    end_time_rsa = time.time()
    decryption_time_rsa = end_time_rsa - start_time_rsa
    memory_use_end_rsa = python_process.memory_info()[0] / 2. ** 30
#  10 for Kb 30 fo Gb
    memory_used_rsa = abs(memory_use_end_rsa - memory_use_start_rsa)

    print('Memory Used RSA:', memory_used_rsa)
    print('RSA Decrypted text:', decrypted_text)
    print('RSA Encryption Time:', encryption_time_rsa)
    print('RSA Decryption Time:', decryption_time_rsa)

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
# 30 for Gb 10 for Gb

# Measure CPU
    initial_ecc_cpu_time = psutil.cpu_times()

# Generate the ECC KeyPair
    generate_key_pair_ecc()

# Continue with ECC encryption and decryption
    public_key_file_ecc = 'public_key_ECC.pem'
    private_key_file_ecc = 'private_key_ECC.pem'
# Encrypt data and measure the performance
    start_time_ecc = time.time()
    shared_key_ecc = generate_shared_key_ecc(private_key_file_ecc, public_key_file_ecc)
    ciphertext_ecc = encrypt_data_ecc(plaintext, shared_key_ecc)

    end_time_ecc = time.time()
    encryption_time_ecc = end_time_ecc - start_time_ecc
    print('Ciphertext ECC:', ciphertext_ecc)
# Decrypt data and measure the performance
    start_time_ecc = time.time()
    decrypted_text_ecc = decrypt_data_ecc(ciphertext_ecc, private_key_file_ecc, public_key_file_ecc)
    end_time_ecc = time.time()
    decryption_time_ecc = end_time_ecc - start_time_ecc
#  Get Memory details
    memory_use_end_ecc = python_process.memory_info()[0] / 2. ** 30
#  30 for Gb 10 for Kb
    memory_used_ecc = abs(memory_use_end_ecc - memory_use_start_ecc)

    print('Memory Used ECC:', memory_used_ecc)
    print('ECC Decrypted text:', decrypted_text_ecc)
    print('ECC Encryption Time:', encryption_time_ecc)
    print('ECC Decrypted Time:', decryption_time_ecc)

    final_ecc_cpu_time = psutil.cpu_times()
    cpu_usage_ecc = psutil.cpu_percent(interval=None, percpu=False)
    print(f"Initial ECC CPU Time: {initial_ecc_cpu_time}")
    print(f"Final ECC CPU time: {final_ecc_cpu_time}")
    print(f"ECC CPU usage: {cpu_usage_ecc}%")

    print('________________________________________________________________________________')

    if encryption_time_rsa != 0.0:
        percentage_time_encryption = abs((encryption_time_rsa - encryption_time_ecc) / encryption_time_rsa * 100)
        print(f"The Percentage time for encryption difference is: {percentage_time_encryption:.2f}%")
        if encryption_time_rsa < encryption_time_ecc:
            print('RSA is the clear winner with encryption')
        else:
            print('ECC is the clear winner with encryption')
    else:
        print('Error: Cannot calculate percentage time for encryption. Division by zero.')

    if decryption_time_rsa != 0.0:
        percentage_time_decryption = abs((decryption_time_rsa - decryption_time_ecc) / decryption_time_rsa * 100)
        print(f"The Percentage time for decryption difference is: {percentage_time_decryption:.2f}%")
        if decryption_time_rsa < decryption_time_ecc:
            print('RSA is the clear winner with decryption')
        else:
            print('ECC is the clear winner with decryption')
    else:
        print('Error: Cannot calculate percentage time for decryption. Division by zero.')

    if memory_used_rsa > memory_used_ecc:
        print('RSA used more memory than ECC by:', memory_used_rsa - memory_used_ecc)
    else:
        print('ECC used more memory than RSA by:', memory_used_ecc - memory_used_rsa)
    if memory_used_rsa != 0:
        memory_diff = abs((memory_used_ecc - memory_used_rsa) / memory_used_rsa * 100)
        print(f"Percentage memory difference: {memory_diff}%")

    return memory_used_rsa, memory_used_ecc, encryption_time_rsa, encryption_time_ecc, decryption_time_rsa, \
        decryption_time_ecc, cpu_usage_rsa, cpu_usage_ecc
