import streamlit as st
# from streamlit_extras.colored_header import colored_header
from markdownlit import mdlit

# colored_header(
#     label="Tugas Kriptografi",
#     description="Dirchamsyah | A11.2021.13610 | A11.4302",
#     color_name="blue-70",
# )
mdlit(
        """Aplikasi yang dibuat untuk memenuhi kebutuhan pengerjaan tugas mata kuliah Kriptografi. Aplikasi ini menyajikan berbagai algoritma seperti Homofonic Cipher, Playfair Cipher, dan Stream Cipher, dan Block Cipher - CBC (Cipher Block Chaining)
    """
)
tab1, tab2, tab3, tab4 = st.tabs(["🔐Homofonic", "🔐Playfair",'🔐Stream','🔐Block-CBC'])
tab1.write("Homofonic Cipher adalah metode substitusi di mana setiap karakter dalam plain teks dapat dipetakan ke beberapa karakter yang berbeda dalam cipher teks. Dengan memperkenalkan variasi dalam representasi karakter, Homofonic Cipher meningkatkan keamanan enkripsi. Namun, penggunaan lebih banyak simbol dapat membuat cipher teks menjadi lebih panjang.")
tab2.write("Playfair Cipher adalah teknik substitusi di mana pasangan huruf dienkripsi dengan menggunakan aturan tertentu. Biasanya digunakan untuk mengenkripsi bigram (pasangan dua huruf), Playfair Cipher menciptakan matriks kunci untuk mentransformasikan huruf-huruf tersebut.")
tab3.write("Stream Cipher adalah metode enkripsi yang mengenkripsi setiap bit dari plain teks dengan melakukan operasi XOR terhadap bit yang sesuai dari kunci. Operasi XOR menghasilkan cipher teks dengan menggunakan logika XOR, di mana setiap bit dalam plain teks akan diubah berdasarkan nilai bit yang sesuai dalam kunci, memberikan tingkat keamanan yang baik untuk komunikasi yang menggunakan algoritma ini.")
tab4.write("Block cipher adalah salah satu jenis algoritma kriptografi simetris yang mengenkripsi dan mendekripsi data dalam bentuk blok-blok tetap, salah satu mode operasi yang umum digunakan bersama dengan block cipher adalah Cipher Block Chaining (CBC). Mode operasi CBC melibatkan penggunaan initial vector (IV) yang merupakan nilai acak yang diperlukan untuk memulai proses enkripsi. ")