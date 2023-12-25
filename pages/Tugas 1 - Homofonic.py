import streamlit as st
import pandas as pd
import random
# from streamlit_extras.colored_header import colored_header


# Fungsi untuk melakukan enkripsi
def encrypt_homophonic(plaintext, substitution_matrix):
    ciphertext = ''

    for char in plaintext:
        if char.upper() in substitution_matrix:
            substitutes = substitution_matrix[char.upper()]
            ciphertext += substitutes[random.randint(0, len(substitutes) - 1)]
        else:
            ciphertext += char

    return ciphertext

# Fungsi untuk melakukan dekripsi
def decrypt_homophonic(ciphertext, substitution_matrix):
    plaintext = ''
    i = 0

    while i < len(ciphertext):
        found = False
        for original_char, substitutes in substitution_matrix.items():
            for sub in substitutes:
                if ciphertext[i:i+2] == sub:
                    plaintext += original_char
                    found = True
                    i += 2
                    break
            if found:
                break
        if not found:
            plaintext += ciphertext[i]
            i += 1

    return plaintext

def main():
    # colored_header(
    # label="Tugas 1 - Homofonic",
    # description="Dirchamsyah | A11.2021.13610 | A11.4302",
    # color_name="blue-70",
    # )

    # Matriks substitusi homofonik yang sudah ditentukan
    substitution_matrix = {
        'A': ['AA', 'AB', 'AC'],
        'B': ['BA', 'BB', 'BC'],
        'C': ['CA', 'CB', 'CC'],
        'D': ['DA', 'DB', 'DC'],
        'E': ['EA', 'EB', 'EC'],
        'F': ['FA', 'FB', 'FC'],
        'G': ['GA', 'GB', 'GC'],
        'H': ['HA', 'HB', 'HC'],
        'I': ['IA', 'IB', 'IC'],
        'J': ['JA', 'JB', 'JC'],
        'K': ['KA', 'KB', 'KC'],
        'L': ['LA', 'LB', 'LC'],
        'M': ['MA', 'MB', 'MC'],
        'N': ['NA', 'NB', 'NC'],
        'O': ['OA', 'OB', 'OC'],
        'P': ['PA', 'PB', 'PC'],
        'Q': ['QA', 'QB', 'QC'],
        'R': ['RA', 'RB', 'RC'],
        'S': ['SA', 'SB', 'SC'],
        'T': ['TA', 'TB', 'TC'],
        'U': ['UA', 'UB', 'UC'],
        'V': ['VA', 'VB', 'VC'],
        'W': ['WA', 'WB', 'WC'],
        'X': ['XA', 'XB', 'XC'],
        'Y': ['YA', 'YB', 'YC'],
        'Z': ['ZA', 'ZB', 'ZC'],
    }

    substitution_df = pd.DataFrame(substitution_matrix)

    # Menampilkan DataFrame pada Streamlit
    st.write("Substitution Matrix:")
    st.dataframe(substitution_df)


    pilih = st.radio('Pilih Opsi Berikut:', ['Enkripsi','Dekripsi'])

    if (pilih=='Enkripsi'):
        plaintext = st.text_input("Masukkan plaintext: ")
        encrypted_text = encrypt_homophonic(plaintext, substitution_matrix)

        encrypt_button = st.button("Enkripsi")

        if encrypt_button:
            st.write("Ciphertext:", encrypted_text)
    else:
        
        ciphertext = st.text_input("Masukkan ciphertext: ")
        decrypted_text = decrypt_homophonic(ciphertext.upper(), substitution_matrix)

        decrypt_button = st.button("Dekripsi")

        if decrypt_button:
            st.write("Plaintext:", decrypted_text)

if __name__ == '__main__':
    main()