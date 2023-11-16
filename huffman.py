import heapq
from collections import defaultdict

class Node:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def _lt_(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return
    if root.char is not None:
        huffman_codes[root.char] = current_code
    build_huffman_codes(root.left, current_code + '0', huffman_codes)
    build_huffman_codes(root.right, current_code + '1', huffman_codes)

def huffman_encoding(data):
    if not data:
        return "", None
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1
    root = build_huffman_tree(freq_dict)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data:
        return ""
    decoded_data = ""
    current = root
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            decoded_data += current.char
            current = root
    return decoded_data

if __name__ == "_main_":
    data = "this is an example for huffman encoding"
    encoded_data, tree = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Decoded data: {decoded_data}")