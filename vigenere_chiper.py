def enkripsi(plaintext, key):
    ciphertext = ''
    key_len = len(key)

    for i in range(len(plaintext)):
        plaintext_ord = ord(plaintext[i])
        key_ord = ord(key[i % key_len])  # Menggunakan operasi modulus untuk mengulang kunci jika lebih pendek
        enkripsi_char = chr((plaintext_ord ^ key_ord) % (126 - 32 + 1) + 32)
        ciphertext += enkripsi_char

    return ciphertext

def dekripsi(ciphertext, key):
    return enkripsi(ciphertext, key)  # Dekripsi sama dengan enkripsi

# Fungsi untuk meng-convert string ke binary
def string_ke_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

# Fungsi untuk meng-convert binary ke string
def binary_ke_string(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8) if len(b[i:i+8]) == 8)

while True:
    print("\nMenu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Exit")
    
    choice = input("Masukkan pilihan anda (1, 2, or 3): ")

    if choice == '1':
        plaintext = input("\nPlaintext: ")
        
        # Pisahkan binary plaintext menjadi tiap karakter
        binary_plaintext_list = [string_ke_binary(plaintext)[i:i+8] for i in range(0, len(string_ke_binary(plaintext)), 8)]
        
        # Pisahkan decimal plaintext menjadi tiap karakter
        decimal_plaintext_list = [ord(c) for c in plaintext]

        print(f'\nBinary plaintext: {binary_plaintext_list}')
        print(f'\nDecimal plaintext: {decimal_plaintext_list}')
        
        print("\n=================================================\n")
        
        key = input("Key: ")
        
        # Pisahkan binary key menjadi tiap karakter
        binary_key_list = [string_ke_binary(key)[i:i+8] for i in range(0, len(string_ke_binary(key)), 8)]

        # Pisahkan decimal key menjadi tiap karakter
        decimal_key_list = [ord(c) for c in key]

        print(f'\nBinary key: {binary_key_list}')
        print(f'\nDecimal key: {decimal_key_list}')
        
        print("\n=================================================\n")
        
        enkripsi_text = enkripsi(plaintext, key)
        binary_ciphertext = string_ke_binary(enkripsi_text)

        # Pisahkan binary ciphertext menjadi tiap karakter
        binary_ciphertext_list = [binary_ciphertext[i:i+8].rjust(8, '0') for i in range(0, len(binary_ciphertext), 8)]

        # Pisahkan decimal ciphertext menjadi tiap karakter
        decimal_ciphertext_list = [int(binary_ciphertext_list[i], 2) for i in range(len(binary_ciphertext_list))]

        print(f'Chipertext: {enkripsi_text}')
        print(f'\nBinary ciphertext: {binary_ciphertext_list}')
        print(f'\nDecimal ciphertext: {decimal_ciphertext_list}')
        
        print("\n=================================================")

    elif choice == '2':
        ciphertext = input("\nCiphertext: ")
        
        # Pisahkan binary plaintext menjadi tiap karakter
        binary_chipertext_list = [string_ke_binary(ciphertext)[i:i+8] for i in range(0, len(string_ke_binary(ciphertext)), 8)]
        
        # Pisahkan decimal plaintext menjadi tiap karakter
        decimal_chipertext_list = [ord(c) for c in ciphertext]
        
        print(f'\nBinary ciphertext: {binary_ciphertext_list}')
        print(f'\nDecimal ciphertext: {decimal_ciphertext_list}')
        
        print("\n=================================================\n")
        
        key = input("Key: ")
        
        # Pisahkan binary key menjadi tiap karakter
        binary_key_list = [string_ke_binary(key)[i:i+8] for i in range(0, len(string_ke_binary(key)), 8)]

        # Pisahkan decimal key menjadi tiap karakter
        decimal_key_list = [ord(c) for c in key]

        print(f'\nBinary key: {binary_key_list}')
        print(f'\nDecimal key: {decimal_key_list}')    
        
        print("\n=================================================\n")    
        
        dekripsi_text = dekripsi(ciphertext, key)
        binary_plaintext = string_ke_binary(dekripsi_text)

        # Pisahkan binary plaintext menjadi tiap karakter
        binary_plaintext_list = [binary_plaintext[i:i+8].rjust(8, '0') for i in range(0, len(binary_plaintext), 8)]

        # Pisahkan decimal plaintext menjadi tiap karakter
        decimal_plaintext_list = [int(binary_plaintext_list[i], 2) for i in range(len(binary_plaintext_list))]

        print(f'Plaintext: {dekripsi_text}')
        print(f'\nBinary plaintext: {binary_plaintext_list}')
        print(f'\nDecimal plaintext: {decimal_plaintext_list}')
        
        print("\n=================================================\n")  

    elif choice == '3':
        print("\nKeluar dari program.")
        print("\n=================================================\n")  
        break

    else:
        print("Pilihan tidak valid, masukkan 1, 2, atau 3.")