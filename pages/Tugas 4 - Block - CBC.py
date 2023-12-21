import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header

def display_table(data):
    st.table(data)

def text_to_binary(text):
    # Fungsi ini mengonversi teks ke biner ASCII
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary_str):
    # Fungsi ini mengonversi biner ASCII ke teks
    text_result = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text_result

def xor_binary(bin_str1, bin_str2):
    # Fungsi ini melakukan operasi XOR pada dua string biner
    return ''.join('1' if a != b else '0' for a, b in zip(bin_str1, bin_str2))

def wrap_4bit(binary_str):
    # Menambahkan wrapping 4 bit pada string biner dengan memindahkan bit pertama ke belakang
    wrapped_binary = ''.join(binary_str[i+1:i+4] + binary_str[i] for i in range(0, len(binary_str), 4))
    return wrapped_binary.strip()

def is_binary_and_length_4(value):
    try:
        int(value, 2)  # Coba mengonversi ke integer dari biner
        return len(value) == 4
    except ValueError:
        return False

def encrypt_cbc(plaintext, key, iv):
    # Pastikan panjang kunci dan IV sesuai
    if len(key) != 4 or len(iv) != 4:
        raise ValueError("Panjang kunci dan IV harus 4 bit")

    ciphertext = ''
    previous_block = iv
    result_values = []
    for i in range(0, len(plaintext), len(key)):
        # Pemisahan teks menjadi blok-blok sesuai dengan panjang kunci
        block = plaintext[i:i+len(key)]

        # XOR dengan blok sebelumnya (atau IV untuk blok pertama)
        block_xor = xor_binary(block, previous_block)

        # XOR hasil dengan kunci
        key_xor = xor_binary(block_xor, key)

        wrap = wrap_4bit(key_xor)



        result_values.append({
            'P(i)': block,
            'C(i)': previous_block,
            'XOR(block)': block_xor,
            'K' : key,
            'XOR(key)': key_xor,
            'WRAP': wrap
        })

        encrypted_block = wrap
        # Simpan blok untuk digunakan sebagai IV pada blok berikutnya
        previous_block = encrypted_block

        # Tambahkan blok terenkripsi ke ciphertext
        ciphertext += encrypted_block

    result_values.append({'ciphertext': ciphertext})

    df = pd.DataFrame(result_values)
    
    return df



def main():
    colored_header(
        label="Tugas 4 - Block - CBC",
        description="Dirchamsyah | A11.2021.13610 | A11.4302",
        color_name="blue-70",
    )

    st.write('Enkripsi Block Cipher - CBC')
    plaintext = st.text_input("Masukkan plaintext : ")
    key = st.text_input("Masukkan kunci (*4 bit biner): ")
    iv = st.text_input("Masukkan initial vector / IV (*4 bit biner): ")

    input_values = []
    

    encrypt_button = st.button("Enkripsi")


    if encrypt_button:
        # Periksa kondisi input
        
        if is_binary_and_length_4(key) and is_binary_and_length_4(iv):
            
            plaintext_biner = text_to_binary(plaintext)

            

            rs = encrypt_cbc(plaintext_biner, key, iv)

            st.subheader("Ciphertext :")
            st.write( rs['ciphertext'].iloc[-1])

            with st.expander("Lihat Detail"):

                st.subheader("Input Data Values :")
                input_values.append({
                    'Plaintext': plaintext,
                    'Plaintext Biner': plaintext_biner,
                    'Key': key,
                    'Initial Vector' : iv
                })

                df = pd.DataFrame(input_values)
                transposed_df = df.transpose()
                display_table(transposed_df)
                


                st.subheader("Block Ciphering - CBC  :")
                result_df = rs.drop(index=rs.index[-1], columns='ciphertext')
                transposed_rs = result_df.transpose()

                display_table(transposed_rs)

        else:
            st.warning("Input kunci dan iv harus berupa biner dan berjumlah 4 bit.")
        
    #     plaintext_binary = ascii_to_binary(plaintext)
    #     key_binary = key_repeated(plaintext, key)
    #     encrypted_text = xor_cipher(plaintext, key)
    #     encrypted_text_wrap = wrap_4bit(encrypted_text)

    #     st.write('Wrapping Ciphertext : ', encrypted_text_wrap)

    #     with st.expander("Lihat Detail"):
    #         data = {'Binary Plaintext': [plaintext_binary], 'Binary Repeated Key': [key_binary], 'Ciphertext': [encrypted_text],'Wrapping Ciphertext ': [encrypted_text_wrap] }
    #         df = pd.DataFrame(data)
            
    #         transposed_df = df.transpose()
    #         display_table(transposed_df)

if __name__ == '__main__':
    main()