# ==========================================
# NODE HUFFMAN TREE
# Struktur data ini merepresentasikan setiap simpul dalam pohon Huffman
# ==========================================

class Node:

    # Constructor
    def __init__(self, char, freq):

        # Karakter yang disimpan oleh node, jika node ini adalah daun
        self.char = char

        # Frekuensi kemunculan karakter tersebut
        self.freq = freq

        # Child kiri dari node
        self.left = None

        # Child kanan dari node
        self.right = None

    # Mengecek apakah node ini adalah daun (tidak punya anak)
    def is_leaf(self):
        return self.left is None and self.right is None