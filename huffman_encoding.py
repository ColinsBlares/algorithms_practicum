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


text = "Errare humanum est."
huffman_encode(text)
