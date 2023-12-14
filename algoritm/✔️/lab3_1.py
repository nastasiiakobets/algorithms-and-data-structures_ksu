class ArrayTree:
    def __init__(self, size):
        # Конструктор класу, створює масив заданого розміру для представлення дерева
        self.tree = [None] * size

    def insert(self, index, value):
        # Метод для вставки значення в масив на заданий індекс
        self.tree[index] = value

    def get_left_child(self, index):
        # Метод для отримання значення лівого вузла за його індексом
        left_child_index = 2 * index + 1
        if left_child_index < len(self.tree):
            return self.tree[left_child_index]
        return None

    def get_right_child(self, index):
        # Метод для отримання значення право вузла за його індексом
        right_child_index = 2 * index + 2
        if right_child_index < len(self.tree):
            return self.tree[right_child_index]
        return None

    def left_to_right_traversal(self, index):
        # Обхід дерева зліва направо
        if index < len(self.tree) and self.tree[index] is not None:
            self.left_to_right_traversal(2 * index + 1)  # left child
            print(self.tree[index], end=" ")
            self.left_to_right_traversal(2 * index + 2)  # right child

    def top_to_bottom_traversal(self, index):
        # Обхід дерева зверху вниз
        if index < len(self.tree) and self.tree[index] is not None:
            print(self.tree[index], end=" ")
            self.top_to_bottom_traversal(2 * index + 1)  # left child
            self.top_to_bottom_traversal(2 * index + 2)  # right child

    def bottom_to_top_traversal(self, index):
        # Обхід дерева знизу вверх
        if index < len(self.tree) and self.tree[index] is not None:
            self.bottom_to_top_traversal(2 * index + 1)  # left child
            self.bottom_to_top_traversal(2 * index + 2)  # right child
            print(self.tree[index], end=" ")

# Створення об'єкту класу ArrayTree з розміром 10
tree = ArrayTree(10)

# Вставка значень у дерево на певні індекси
tree.insert(0, 1)
tree.insert(1, 2)
tree.insert(2, 3)
tree.insert(3, 4)
tree.insert(4, 5)

# Обхід дерева зліва направо
print("Left to Right Traversal:")
tree.left_to_right_traversal(0)
print("\n")

# Обхід дерева зверху вниз
print("Top to Bottom Traversal:")
tree.top_to_bottom_traversal(0)
print("\n")

# Обхід дерева знизу вверх
print("Bottom to Top Traversal:")
tree.bottom_to_top_traversal(0)
print("\n")