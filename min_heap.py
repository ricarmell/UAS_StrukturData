from huffman_tree import Node

# ==========================================
# MIN HEAP
# Struktur data ini digunakan untuk mengambil karakter dengan frekuensi paling kecil
# sehingga proses pembentukan pohon Huffman menjadi lebih teratur
# ==========================================

class MinHeap:

    def __init__(self):
        # List dipakai sebagai tempat penyimpanan data heap
        self.heap = []

    # Mengambil index parent dari suatu node
    def parent(self, i):
        return (i - 1) // 2

    # Mengambil index anak kiri
    def left(self, i):
        return 2 * i + 1

    # Mengambil index anak kanan
    def right(self, i):
        return 2 * i + 2

    # Menukar posisi dua node dalam heap
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Menambahkan node ke heap
    def insert(self, node):
        self.heap.append(node)

        i = len(self.heap) - 1

        # Naikkan node ke atas jika frekuensinya lebih kecil dari parent
        while i != 0 and self.heap[self.parent(i)].freq > self.heap[i].freq:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # Menata ulang heap setelah penghapusan
    def heapify(self, i):
        smallest = i

        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l].freq < self.heap[smallest].freq:
            smallest = l

        if r < len(self.heap) and self.heap[r].freq < self.heap[smallest].freq:
            smallest = r

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    # Mengambil node dengan frekuensi terkecil dari heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)

        return root

    # Mengembalikan jumlah node yang ada di heap
    def size(self):
        return len(self.heap)