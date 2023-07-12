# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetim

import random
import datetime
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
lst = []
for key in my_favorite_songs_dict.keys() :  
    lst.append(key)  # создали список всех песен                         
lst_3 = random.sample(lst, 3)  # список трёх случайных песен
print(lst_3)
l = []
for i in lst_3 :
    l.append(my_favorite_songs_dict[i])  # список со временем звучания песен
print(l)
m = int(l[0]) + int(l[1]) + int(l[2]) #  посчитали минуты
s = (l[0] - int(l[0])) * 100 + (l[1] - int(l[1])) * 100 + (l[2] - int(l[2])) * 100 # посчитали секунды
res = m * 60 + s # привели всё к секундам
total_res = round(res // 60 + (res % 60) / 100, 2)
print('Три песни звучат', total_res, 'минут')
t = str(total_res).split('.')
if len(t[1]) == 1 :  # доп. проверка на корректность
    t[1] += '0'      # последующего вывода времени
total_t = datetime.time(0, int(t[0]), int(t[1]))
print('Три песни звучат', total_t, 'минут')