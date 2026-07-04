# ==========================================
# PROGRAM UTAMA
# Aplikasi Kompresi Teks Huffman Coding
# ==========================================

# Import modul yang dibutuhkan
from hash_table import HashTable  # Struktur data tabel hash untuk menghitung frekuensi
from huffman_tree import Node  # Struktur data node pohon Huffman
from min_heap import MinHeap  # Struktur data heap minimum untuk memilih node dengan frekuensi kecil
from encoder import build_codes, encode  # Fungsi untuk membuat kode Huffman dan meng-encode teks
from decoder import decode  # Fungsi untuk meng-decode kode Huffman kembali ke teks

5263
def build_huffman_tree(text):
    # 1. Gunakan HashTable untuk menghitung frekuensi setiap karakter
    ht = HashTable()

    # Cek setiap karakter dalam teks dan tambahkan ke tabel hash
    for ch in text:
        ht.insert(ch)

    # Ambil hasil frekuensi karakter dalam bentuk dictionary
    freq = ht.get_frequency()

    # 2. Gunakan MinHeap agar karakter dengan frekuensi paling kecil diproses dulu
    heap = MinHeap()

    # Masukkan setiap karakter sebagai node ke dalam heap
    for ch, f in freq.items():
        heap.insert(Node(ch, f))

    # 3. Bangun pohon Huffman dengan menggabungkan dua node paling kecil
    while heap.size() > 1:
        left = heap.extract_min()   # node terkecil pertama
        right = heap.extract_min()  # node terkecil kedua

        # Buat parent baru yang frekuensinya adalah jumlah dari dua child
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right

        heap.insert(parent)

    # 4. Akar pohon Huffman
    root = heap.extract_min()
    return freq, root


def main():
    # Menyimpan semua teks yang sudah di-encode dalam bentuk list
    data_list = []

    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Input teks")
        print("2. Lihat hasil encode semua teks")
        print("3. Decode teks tertentu")
        print("4. Lihat kode Huffman teks tertentu")
        print("5. Lihat frekuensi karakter teks tertentu")
        print("6. Keluar")

        pilihan = input("Pilih menu : ").strip()

        if pilihan == "1":
            # Minta pengguna memasukkan teks sampai teks tidak kosong
            while True:
                text = input("Masukkan teks : ").strip()
                if text:
                    break
                print("Teks kosong, silakan masukkan lagi.")

            # Buat pohon Huffman untuk teks tersebut
            freq, root = build_huffman_tree(text)
            codes = build_codes(root)
            encoded_text = encode(text, codes)

            # Simpan hasil proses teks ini agar bisa dipakai lagi nanti
            data_list.append({
                "text": text,
                "freq": freq,
                "root": root,
                "codes": codes,
                "encoded": encoded_text,
            })

            print("\nTeks berhasil di-encode.")

        elif pilihan == "2":
            # Tampilkan semua teks yang sudah di-encode
            if not data_list:
                print("Belum ada teks yang di-encode.")
                continue

            print("\n===== Hasil Encoding =====")
            for index, item in enumerate(data_list, start=1):
                print(f"{index}. {item['text']} -> {item['encoded']}")

        elif pilihan == "3":
            # Decode teks yang sudah pernah di-encode sebelumnya
            if not data_list:
                print("Belum ada teks yang di-encode.")
                continue

            try:
                nomor = int(input("Pilih nomor teks yang ingin di-decode : ").strip())
            except ValueError:
                print("Input harus berupa angka.")
                continue

            if 1 <= nomor <= len(data_list):
                selected = data_list[nomor - 1]
                decoded = decode(selected["encoded"], selected["root"])
                print(f"\n===== Hasil Decoding teks {nomor} =====")
                print(decoded)
                print(f"\nTeks asli dari hasil encode teks {nomor} :")
                print(selected["text"])
            else:
                print("Nomor teks tidak valid.")

        elif pilihan == "4":
            # Tampilkan kode Huffman untuk teks tertentu
            if not data_list:
                print("Belum ada teks yang di-encode.")
                continue

            try:
                nomor = int(input("Pilih nomor teks : ").strip())
            except ValueError:
                print("Input harus berupa angka.")
                continue

            if 1 <= nomor <= len(data_list):
                selected = data_list[nomor - 1]
                print(f"\n===== Kode Huffman teks {nomor} =====")
                for k, v in selected["codes"].items():
                    print(k, "=", v)
            else:
                print("Nomor teks tidak valid.")

        elif pilihan == "5":
            # Tampilkan frekuensi karakter, artinya berapa kali setiap karakter muncul
            if not data_list:
                print("Belum ada teks yang di-encode.")
                continue

            try:
                nomor = int(input("Pilih nomor teks : ").strip())
            except ValueError:
                print("Input harus berupa angka.")
                continue

            if 1 <= nomor <= len(data_list):
                selected = data_list[nomor - 1]
                print(f"\n===== Frekuensi karakter teks {nomor} =====")
                print("Artinya: berapa kali setiap karakter muncul dalam teks")
                for k, v in selected["freq"].items():
                    print(k, ":", v)
            else:
                print("Nomor teks tidak valid.")

        elif pilihan == "6":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()