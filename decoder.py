# ==========================================
# DECODER
# Bagian ini berfungsi mengubah kode Huffman kembali menjadi teks asli
# ==========================================

# Fungsi decode membaca bit-bit hasil encode satu per satu
# lalu menelusuri pohon Huffman sampai menemukan satu karakter

def decode(encoded, root):

    hasil = ""

    # Mulai dari akar pohon Huffman
    current = root

    # Baca setiap bit hasil encode
    for bit in encoded:

        # Jika bit 0, bergerak ke kiri
        if bit == "0":
            current = current.left

        # Jika bit 1, bergerak ke kanan
        else:
            current = current.right

        # Jika sudah sampai daun, berarti satu karakter ditemukan
        if current.left is None and current.right is None:
            hasil += current.char

            # Kembali ke akar untuk membaca karakter berikutnya
            current = root

    return hasil