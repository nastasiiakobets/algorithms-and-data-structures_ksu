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
        self.min_element = float('inf')

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        if data < self.min_element:
            self.min_element = data

    def pop(self):
        if self.is_empty():
            print("Список порожній. Неможливо вилучити елемент.")
            return None

        popped_data = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        if popped_data == self.min_element:
            self.update_min_element()

        return popped_data

    def update_min_element(self):
        if self.is_empty():
            self.min_element = float('inf')
        else:
            current = self.head
            self.min_element = current.data
            while current:
                if current.data < self.min_element:
                    self.min_element = current.data
                current = current.next

    def find_min_element(self):
        if self.is_empty():
            print("Список порожній. Неможливо знайти мінімальний елемент.")
            return None
        else:
            return self.min_element

    def display(self):
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
doubly_linked_list = DoublyLinkedList()

# Введення елементів списку з клавіатури
for _ in range(size):
    element = int(input("Введіть елемент списку: "))
    doubly_linked_list.append(element)

print("Створений двозв'язаний список:")
doubly_linked_list.display()

# Вимірювання часу перед видаленням елементу та виведенням мінімального елементу
start_time = time.time()

# Виведення мінімального елементу перед видаленням
print("Мінімальний елемент у списку:", doubly_linked_list.find_min_element())

# Вилучення елементу та виведення мінімального елементу після видалення
removed_element = doubly_linked_list.pop()
print(f"Вилучено елемент: {removed_element}")
print("Мінімальний елемент у списку після видалення:", doubly_linked_list.find_min_element())

# Вимірювання часу після видалення та виведенням зміненого списку
end_time = time.time()
print("Двозв'язаний список після видалення:")
doubly_linked_list.display()

# Виведення часу виконання
print(f"Час виконання: {end_time - start_time} секунд")