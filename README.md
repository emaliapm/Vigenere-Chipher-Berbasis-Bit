# Vigenere-Chipher-Berbasis-Bit
Program ini mengimplementasikan algoritma enkripsi dan dekripsi XOR sederhana menggunakan Python. XOR (exclusive OR) digunakan untuk melakukan kedua operasi enkripsi dan dekripsi.

## Algoritma:

### Enkripsi:
1. Konversi setiap karakter dari plaintext ke nilai ASCII menggunakan `ord()`.
2. Konversi setiap karakter dari kunci (key) ke nilai ASCII juga.
3. Melakukan operasi XOR antara nilai ASCII karakter plaintext dan karakter kunci.
4. Konversi hasil XOR kembali menjadi karakter menggunakan `chr()`.
5. Ambil nilai ASCII hasil XOR modulo rentang karakter yang valid (32 hingga 126).
6. Ulangi proses tersebut untuk setiap karakter dalam plaintext.

### Dekripsi:
1. Dekripsi menggunakan operasi XOR yang sama dengan enkripsi. Karena XOR adalah operasi yang dapat dibalik (A XOR B XOR B = A), proses enkripsi dapat digunakan untuk dekripsi.

## Fungsi Tambahan:

### `string_ke_binary(s)`:
- Mengonversi setiap karakter dari string ke representasi biner 8-bit.
- Menggabungkan representasi biner untuk setiap karakter dan mengembalikan string biner.

### `binary_ke_string(b)`:
- Mengonversi string biner kembali ke string teks menggunakan representasi ASCII.

## Struktur Program:

1. **Menu Utama:**
   - Menampilkan menu dengan opsi untuk enkripsi, dekripsi, dan keluar.
   - Menggunakan loop `while True` untuk menjalankan program secara berulang.

2. **Opsi 1 (Enkripsi):**
   - Menerima input pengguna untuk plaintext dan key.
   - Mengonversi plaintext dan key ke bentuk biner dan desimal.
   - Melakukan enkripsi menggunakan fungsi `enkripsi`.
   - Menampilkan hasil enkripsi dalam bentuk text, biner, dan desimal.

3. **Opsi 2 (Dekripsi):**
   - Menerima input pengguna untuk ciphertext dan key.
   - Mengonversi ciphertext dan key ke bentuk biner dan desimal.
   - Melakukan dekripsi menggunakan fungsi `dekripsi`.
   - Menampilkan hasil dekripsi dalam bentuk text, biner, dan desimal.

4. **Opsi 3 (Keluar):**
   - Mengakhiri program ketika pengguna memilih untuk keluar.
