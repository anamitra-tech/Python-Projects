import heapq
from collections import Counter

# Node structure
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # For priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Generate Huffman codes recursively
def generate_codes(node, prefix='', code_dict={}):
    if node is None:
        return
    if node.char is not None:  # Leaf node
        code_dict[node.char] = prefix
    generate_codes(node.left, prefix + '0', code_dict)
    generate_codes(node.right, prefix + '1', code_dict)
    return code_dict

# Huffman Encoding
def huffman_encoding(text):
    if not text:
        return {}, ''
    
    # Step 1: Frequency count
    freq_map = Counter(text)
    
    # Step 2: Build priority queue
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    # Step 3: Build Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    root = heap[0]
    
    # Step 4: Generate codes
    huffman_codes = generate_codes(root)
    
    # Step 5: Encode text
    encoded_text = ''.join(huffman_codes[ch] for ch in text)
    
    return huffman_codes, encoded_text

# Example usage
text = "this is an example for huffman encoding"
codes, encoded = huffman_encoding(text)

print("Huffman Codes:")
for char, code in codes.items():
    print(f"'{char}': {code}")
print("\nEncoded Text:")
print(encoded)
