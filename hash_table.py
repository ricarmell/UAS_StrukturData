# ==========================================
# HASH TABLE
# Struktur data ini digunakan untuk menghitung frekuensi setiap karakter
# ==========================================

class HashTable:

    # Constructor
    def __init__(self):
        # Dictionary dipakai sebagai tempat menyimpan data
        # contoh: {'a': 3, 'b': 1}
        self.table = {}

    # Menambahkan karakter ke dalam hash table
    def insert(self, char):

        # Jika karakter sudah ada, tambahkan jumlah kemunculannya
        if char in self.table:
            self.table[char] += 1

        # Jika belum ada, buat data baru dengan nilai awal 1
        else:
            self.table[char] = 1

    # Mengembalikan seluruh data frekuensi karakter
    def get_frequency(self):
        return self.table