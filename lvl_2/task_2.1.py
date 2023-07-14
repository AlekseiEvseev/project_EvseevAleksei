# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

import random

def minimum(arr, n):
    mn = 100  # присвоили значение переменной по максимальной границе списка
    for i in range(n) :     
      if arr[i] <= mn :        
        mn = arr[i]          
    return mn

def maximum(arr, n):
    mx = - 100  # присвоили значение переменной по минимальной границе списка
    for i in range(n) :     
      if arr[i] >= mx :        
        mx = arr[i]          
    return mx

a = random.randint(1, 10)  # длина списка
lst = [random.randint(-100, 100) for _ in range(a)]  # создаём список
print(lst)
print(f'min = {minimum(lst, a)}, max = {maximum(lst, a)}')