# import section
import os
import time
import psutil
from tabulate import tabulate
from MyEncryptRSA import encrypt_data, generate_key_pair_rsa
from MyDecryptRSA import decrypt_data_rsa
from MyEncryptECC import generate_key_pair_ecc, generate_shared_key_ecc, encrypt_data_ecc
from MyDecryptECC import decrypt_data_ecc
import ProcessRun



# Pip section
# pip install cryptography
# Start
if __name__ == '__main__':
    print('Welcome to my first Python application. '
          'The main purpose of this application is to test and illustrate difference in speed with Encryption and '
          'Decryption of RSA and ECC')
    print('________________________________________________________________________________')
    print('Generating RSA Encryption File')
# Running the process with different size input and return memory_used_rsa, memory_used_ecc, encryption_time_RSA, encryption_time_ECC, decryption_time_RSA, decryption_time_ECC, cpu_usage_rsa, cpu_usage_ecc

    results_small_list = []
    results_medium_list = []
    results_large_list = []
    headers = [
        "Memory Used RSA", "Memory Used ECC",
        "Encryption Time RSA", "Encryption Time ECC",
        "Decryption Time RSA", "Decryption Time ECC",
        "CPU Usage RSA", "CPU Usage ECC"
    ]
    for i in range(100):
        result = ProcessRun.execute('Small')
        results_small_list.append(result)
        print(f"Iteration {i}; {result}")


        result = ProcessRun.execute('Medium')
        results_medium_list.append(result)
        print(f"Iteration {i}; {result}")

        result = ProcessRun.execute('Large')
        results_large_list.append(result)
        print(f"Iteration {i}; {result}")
        i = i + 1

    print('Small Input Size:')
    file_path = 'output_table_small.txt'
    tabulated_output = tabulate(results_small_list,headers=headers,numalign="right",stralign="right",floatfmt=".20f")
    print(tabulated_output)
    with open(file_path, 'w') as file:
        file.write(tabulated_output)

    print('Medium Input Size:')
    file_path = 'output_table_medium.txt'
    tabulated_output = tabulate(results_medium_list, headers=headers, numalign="right", stralign="right",
                                floatfmt=".20f")
    print(tabulated_output)
    with open(file_path, 'w') as file:
        file.write(tabulated_output)

    print('Large Input Size:')
    file_path = 'output_table_large.txt'
    tabulated_output = tabulate(results_large_list, headers=headers, numalign="right", stralign="right",
                                floatfmt=".20f")
    print(tabulated_output)
    with open(file_path, 'w') as file:
        file.write(tabulated_output)