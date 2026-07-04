# Program Huffman Coding

Program ini menggunakan algoritma Huffman untuk mengompres teks. Tujuan program ini adalah mengubah teks menjadi kode biner yang lebih pendek untuk karakter yang sering muncul, lalu mengembalikan kode tersebut ke teks asli saat dibutuhkan.

## Alur program
1. Pengguna memasukkan teks.
2. Program menghitung frekuensi setiap karakter.
3. Program membuat pohon Huffman menggunakan struktur data heap.
4. Program membuat kode Huffman untuk setiap karakter.
5. Program meng-encode teks menjadi kode biner.
6. Program dapat melakukan decode untuk mengembalikan kode ke teks asli.

## Struktur data yang digunakan
- HashTable
  - Digunakan untuk menghitung berapa kali setiap karakter muncul.
  - Data disimpan dalam bentuk pasangan key dan value.
- MinHeap
  - Digunakan untuk memilih dua karakter dengan frekuensi paling kecil.
  - Ini membantu membangun pohon Huffman dengan benar.
- Node
  - Merepresentasikan simpul dalam pohon Huffman.
  - Setiap node menyimpan karakter, frekuensi, dan child kiri serta kanan.
- List
  - Digunakan untuk menyimpan beberapa teks yang sudah di-encode.
  - Memudahkan program memilih teks tertentu saat ingin di-decode.

## Cara penggunaan
1. Jalankan program.
2. Pilih menu input teks.
3. Masukkan teks yang ingin diproses.
4. Pilih menu untuk melihat hasil encode, decode, kode Huffman, atau frekuensi karakter.

## Contoh sederhana
Jika teks yang dimasukkan adalah "banana", maka:
- huruf a muncul lebih sering
- huruf b dan n muncul lebih sedikit
- program akan memberi kode yang lebih pendek untuk huruf yang sering muncul