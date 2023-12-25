import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header

def display_table(data):
    st.table(data)

def ascii_to_binary(ascii_str):
    # Mengonversi setiap karakter ASCII menjadi biner 8 bit
    binary_result = ''.join(format(ord(char), '08b') for char in ascii_str)
    return binary_result

def binary_to_ascii(binary_str):
    # Mengonversi biner 8 bit menjadi karakter ASCII
    ascii_result = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return ascii_result

def key_repeated_encrypt(message, key):
    # Mengonversi string ke dalam biner 8 bit
    message_binary = ascii_to_binary(message)
    key_binary = ascii_to_binary(key)

    # Menentukan panjang pesan dan kunci
    message_length = len(message_binary)
    key_length = len(key_binary)

    # Membuat kunci yang panjangnya sama dengan panjang pesan
    repeated_key = key_binary * (message_length // key_length) + key_binary[:message_length % key_length]

    return repeated_key

def key_repeated_decrypt(cipher_binary, key):
    # Mengonversi string ke dalam biner 8 bit
    key_binary = ascii_to_binary(key)

    # Menentukan panjang pesan dan kunci
    key_length = len(key_binary)

    # Membuat kunci yang panjangnya sama dengan panjang pesan terenkripsi
    repeated_key = key_binary * (len(cipher_binary) // key_length) + key_binary[:len(cipher_binary) % key_length]
    
    return repeated_key

def xor_operation(binary_text, repeated_key):
    message_length = len(binary_text)

    # Melakukan operasi XOR pada setiap bit pesan dan kunci
    result_xor = ''.join(str(int(binary_text[i]) ^ int(repeated_key[i])) for i in range(message_length))

    return result_xor


def main():

    colored_header(
    label="Tugas 3 - Stream",
    description="Dirchamsyah | A11.2021.13610 | A11.4302",
    color_name="blue-70",
    )

    pilih = st.radio('Pilih Opsi Berikut:', ['Enkripsi','Dekripsi'])

    if (pilih=='Enkripsi'):

        #Input
        plaintext = st.text_input("Masukkan plaintext: ")
        keytext = st.text_input("Masukkan kunci: ")
        
        #Button
        encrypt_button = st.button("Enkripsi")
        if encrypt_button:
            
            plaintext_binary = ascii_to_binary(plaintext)
            keytext_binary = key_repeated_encrypt(plaintext, keytext)
            xor_result = xor_operation(plaintext_binary, keytext_binary)

            st.write('Ciphertext : ', xor_result)

            with st.expander("Lihat Detail"):
                # Menyimpan data ke DataFrame
                data = {'Binary Plaintext': [plaintext_binary] , 'Binary Repeated Key': [keytext_binary], 'Ciphertext': [xor_result]}
                df = pd.DataFrame(data)
                
                transposed_df = df.transpose()
                display_table(transposed_df)
            
    else:

        #Input
        ciphertext = st.text_input("Masukkan ciphertext: ")
        keytext = st.text_input("Masukkan kunci: ")
        

        #Button
        decrypt_button = st.button("Dekripsi")
        if decrypt_button:

            keytext_binary = key_repeated_decrypt(ciphertext, keytext)
            xor_result = xor_operation(ciphertext, keytext_binary)
            decrypted_text = binary_to_ascii(xor_result)

            st.write('Plaintext : ', decrypted_text)

            with st.expander("Lihat Detail"):
                # Menyimpan data ke DataFrame
                data = {'Ciphertext': [ciphertext] , 'Binary Repeated Key': [keytext_binary], 'XOR Result': [xor_result], 'Plaintext':[decrypted_text]}
                df = pd.DataFrame(data)
                
                transposed_df = df.transpose()
                display_table(transposed_df)

if __name__ == '__main__':
    main()