import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc


def huffman_encode(data):
    freq = Counter(data)
    heap = []

    for char, freq in freq.items():
        heap.append((freq, len(heap), Leaf(char)))

    heapq.heapify(heap)
    count = len(heap)

    while len(heap) > 1:
        freq1, _count1, left = heapq.heappop(heap)
        freq2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if heap:
        [(_, _, root)] = heap
        root.walk(code, "")

    encoded_data = "".join(code[char] for char in data)
    print(len(code), len(encoded_data))
    for char, huff_code in sorted(code.items()):
        print(f"'{char}': {huff_code}")
    print(encoded_data)


def huffman_decode(encoded_data, codes):
    reverse_code = {v: k for k, v in codes.items()}

    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_code:
            decoded_data += reverse_code[current_code]
            current_code = ""

    return decoded_data


encoded_string = "100011110001001101000111111011001010011000010110011010111110"
codes = {
    ' ': '1011',
    '.': '1110',
    'D': '1000',
    'c': '000',
    'd': '001',
    'e': '1001',
    'i': '010',
    'm': '1100',
    'n': '1010',
    'o': '1111',
    's': '011',
    'u': '1101'
}

decoded_string = huffman_decode(encoded_string, codes)
print(decoded_string)
