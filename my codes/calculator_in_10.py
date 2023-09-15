# -*- coding: utf-8 -*-
"""calculator_in_10

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NhsgLD5Bv8Tg3Z6CeTGtSXv_Kd1k64u6
"""

# Калькулятор (перевод) из любой с-мы счисления в десятичную
num_set = '0123456789abcdef'
base = int(input('Enter your base (2-16)\n'))
num = input(f'Enter your number in base {base} number system\n')[::-1]
res = 0
for i in range(len(num)):
    res += num_set.find(num[i].lower()) * (base ** i)
print(f'Decimal number: {res}')

