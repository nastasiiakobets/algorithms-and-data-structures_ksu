import heapq

class HuffmanNode:
    def __init__(self, value, char=None):
        self.value = value
        self.char = char
        self.left = None
        self.right = None

    # Додано метод порівняння для визначення порядку в min-heap
    def __lt__(self, other):
        return self.value < other.value

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(freq, char) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged_node = HuffmanNode(left.value + right.value)
        merged_node.left, merged_node.right = left, right

        heapq.heappush(heap, merged_node)

    return heap[0]

def print_huffman_tree(node, encoding='', separator='-'):
    if node is not None:
        if node.char is not None:
            print(f"Symbol: {node.char}, Frequency: {node.value}, Encoding: {encoding}")

        print_huffman_tree(node.left, encoding + '0')
        print_huffman_tree(node.right, encoding + '1')

# Приклад використання
frequency_dict = {'a': 8, 'b': 3, 'c': 1, 'd': 6}
huffman_tree_root = build_huffman_tree(frequency_dict)

# Виведення на екран створеного бінарного дерева Хафмена
print("Huffman Tree:")
print_huffman_tree(huffman_tree_root)