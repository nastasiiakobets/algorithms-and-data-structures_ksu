import random
import time

n = 20 #1000 #2000 #3000 #4000 #5000 #6000
a = [0] * n

def bubble_sort(arr):
    # Функція сортування бульбашкою
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def generate_random_array(arr):
    # Функція генерації випадкового масиву
    for i in range(len(arr)):
        arr[i] = random.randint(1, 1000)

if __name__ == '__main__':
    generate_random_array(a)
    
    print("Вихідний масив:")
    print(a)
    
    start_time = time.time()
    bubble_sort(a)
    end_time = time.time()

    print("Відсортований масив:")
    print(a)
    
    execution_time = end_time - start_time  # у секундах
    print(f"Час виконання сортування: {execution_time:.6f} с")