import time

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        # Додає новий вузол з даними data до кінця списку.
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        # Додає новий вузол з даними data до початку списку.
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_front(self):
        # Вилучає та повертає елемент з початку списку.
        if self.is_empty():
            print("Список порожній. Неможливо вилучити елемент.")
            return None

        popped_data = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return popped_data

    def pop_back(self):
        # Вилучає та повертає елемент з кінця списку.
        if self.is_empty():
            print("Список порожній. Неможливо вилучити елемент.")
            return None

        popped_data = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return popped_data

    def find_min_element(self):
        # Пошук мінімального елементу у списку.
        if self.is_empty():
            print("Список порожній. Неможливо знайти мінімальний елемент.")
            return None

        current = self.head
        min_element = current.data

        while current:
            if current.data < min_element:
                min_element = current.data
            current = current.next

        return min_element

    def display(self):
        # Виводить вміст списку на екран.
        if self.is_empty():
            print("Список порожній.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Введення розміру списку з клавіатури
size = int(input("Введіть розмір списку: "))
linked_list = DoublyLinkedList()

# Введення елементів списку з клавіатури
for _ in range(size):
    element = int(input("Введіть елемент списку: "))
    linked_list.append(element)

# Вимірювання часу роботи алгоритму
start_time = time.time()

print("Двозв'язаний список після додавання елементів:")
linked_list.display()

removed_front = linked_list.pop_front()
print(f"Вилучено елемент з початку списку: {removed_front}")

removed_back = linked_list.pop_back()
print(f"Вилучено елемент з кінця списку: {removed_back}")

print("Двозв'язаний список після вилучення елементів:")
linked_list.display()

min_element = linked_list.find_min_element()
print(f"Мінімальний елемент у списку: {min_element}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Час виконання алгоритму: {elapsed_time} секунд")