import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq_map = defaultdict(int)
    for char in data:
        freq_map[char] += 1

    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    build_huffman_codes(root.left, current_code + "0", codes)
    build_huffman_codes(root.right, current_code + "1", codes)

def huffman_encode(data):
    if not data:
        return None, None

    root = build_huffman_tree(data)

    codes = {}
    build_huffman_codes(root, "", codes)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root

def huffman_decode(encoded_data, root):
    if not encoded_data or root is None:
        return None

    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

# Example usage:
data = "hello world"
encoded_data, huffman_tree = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, huffman_tree)

print(f"Original data: {data}")
print(f"Encoded data: {encoded_data}")
print(f"Decoded data: {decoded_data}")
