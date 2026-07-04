# ==========================================
# ENCODER
# Bagian ini berfungsi mengubah teks menjadi kode Huffman
# ==========================================

# Fungsi ini menelusuri pohon Huffman dan memberi kode biner untuk setiap karakter
# Contoh: karakter yang sering muncul akan mendapat kode yang lebih pendek

def build_codes(node, code="", codes=None):

    # Jika belum ada dictionary untuk menampung kode, buat baru
    if codes is None:
        codes = {}

    # Jika node kosong, berhenti
    if node is None:
        return codes

    # Jika sampai di daun, simpan kode untuk karakter tersebut
    if node.char is not None:
        codes[node.char] = code

    # Kunjungi anak kiri dengan menambahkan angka 0
    build_codes(node.left, code + "0", codes)

    # Kunjungi anak kanan dengan menambahkan angka 1
    build_codes(node.right, code + "1", codes)

    return codes


# Fungsi ini mengubah teks menjadi kode biner berdasarkan kode Huffman
# contoh: "abc" -> "10011" tergantung pohon yang dibentuk

def encode(text, codes):

    hasil = ""

    for ch in text:
        hasil += codes[ch]

    return hasil