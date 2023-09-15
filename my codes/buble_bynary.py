

import random

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a            

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    index = -1
    while low <= high and index == -1:
        mid = (low + high) // 2
        if arr[mid] == x :
            index = mid
        elif x > arr[mid]:
            low = mid + 1
        else :
            high = mid - 1
    return index

arr = [random.randint(1, 100) for _ in range(10)]
bubble_sort(arr)
print(arr)
x = int(input('Введите число: '))
if x not in arr :
    print('Такого числа нет')
else :
    print('Индекс числа: ', binary_search(arr, x))




