import pandas as pd
import streamlit as st
from streamlit_extras.colored_header import colored_header


def cleaning_key(key):
    allowed_chars = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    result_string = ''.join([char for char in key if char in allowed_chars])
    return result_string

def display_table(data):
    st.table(data)

# Fungsi untuk membuat matriks kunci
def create_playfair_matrix(key):
    key_set = set()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Membuat matrix kosong dengan ukuran 5x5
    playfair_matrix = [['' for _ in range(5)] for _ in range(5)]

    # Mengisi matrix dengan karakter-karakter dari kunci
    index = 0
    for i in range(5):
        for j in range(5):
            while index < len(key):
                char = key[index]
                index += 1

                # Menangani karakter "spasi", "J", atau karakter khusus lainnya
                if char.upper() != 'J' and char.upper() not in key_set:
                    playfair_matrix[i][j] = char.upper()
                    key_set.add(char.upper())
                    break

            if index >= len(key):
                break

    # Mengisi sisa matrix dengan karakter dari alfabet yang belum ada di kunci
    for i in range(5):
        for j in range(5):
            if playfair_matrix[i][j] == '':
                while alphabet[0] in key_set:
                    alphabet = alphabet[1:]

                if alphabet:
                    playfair_matrix[i][j] = alphabet[0]
                    key_set.add(alphabet[0])
                    alphabet = alphabet[1:]

    return playfair_matrix

# Fungsi untuk mencari posisi karakter dalam matriks
def find_position(matrix, target):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == target:
                return row, col

# Fungsi Bigram
def bigram(plaintext):

    length = len(plaintext)
    i=0
    bigram_str = ""
    
    while i < length:
        
        # BIGRAM RULE
        first_char = plaintext[i]
        second_char = plaintext[i + 1] if i + 1 < length else 'Z'
        i += 2

        if first_char == second_char:
            second_char = "Z"
            i -= 1
        bigram_str += first_char+second_char+" "

    return bigram_str

# Fungsi untuk mengenkripsi pesan dengan Playfair Cipher
def encrypt_playfair(plaintext, matrix):
    ciphertext = ""
    length = len(plaintext)
    
    i=0
    
    while i < length:
        
        # BIGRAM RULE
        first_char = plaintext[i]
        second_char = plaintext[i + 1] if i + 1 < length else 'Z'
        i += 2

        if first_char == second_char:
            second_char = "Z"
            i -= 1

        # CARI POSISI PLAINTEXT DI MATRIX
        row1, col1 = find_position(matrix, first_char)
        row2, col2 = find_position(matrix, second_char)

        # BARIS SAMA
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        
        # KOLOM SAMA
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]

        # MENYILANG / DIAGONAL
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext


def main():

    colored_header(
    label="Tugas 2 - Playfair",
    description="Dirchamsyah | A11.2021.13610 | A11.4302",
    color_name="blue-70",
    )

    
    st.subheader("Key Matriks")
    options = ["Defult Key", "Custom Key"]

    # Pilihan dropdown
    selected_option = st.selectbox("Pilih Opsi Key Matriks", options)

    
    with st.expander("Detail"):
        if selected_option=="Defult Key":
            key_string = "Jalan Imam Bonjol Seratus"
            key_string_clean = cleaning_key(key_string.upper())
            define_matrix = create_playfair_matrix(key_string_clean)
            
            st.write("Defult Key :", key_string)
            st.dataframe(define_matrix)

        if selected_option=="Custom Key":
            key_string = st.text_input("Masukkan kata kunci :")
            key_string_clean = cleaning_key(key_string.upper())
            define_matrix = create_playfair_matrix(key_string_clean)
            matrix_button = st.button("Buat Key Matrix")

            # Membuat matrix key
            if matrix_button:
                define_matrix = create_playfair_matrix(key_string_clean)

            st.write("Key String : ", key_string.upper())
            st.write("Key Matrix : ")
            st.dataframe(define_matrix)
    
    
    st.subheader("Playfair Enkripsi")

    # Input pesan
    plaintext = st.text_input("Masukkan plaintext: ").upper()
    encrypt_button = st.button("Enkripsi")

    if encrypt_button:
        if(cleaning_key(plaintext)==''):
            st.warning("Plaintext Kosong/Tidak Valid")
        else:
            plaintext = plaintext.replace(" ", "").replace("J", "I")
            bigramtext = bigram(plaintext)
            ciphertext = encrypt_playfair(plaintext, define_matrix)
            
            st.write("Ciphertext :", ciphertext)

            with st.expander("Lihat Detail"):
                data = {'Plaintext': [plaintext], 'Bigram Rule': [bigramtext], 'Ciphertext': [ciphertext]}
                df = pd.DataFrame(data)
                
                transposed_df = df.transpose()
                display_table(transposed_df)

if __name__ == '__main__':
    main()