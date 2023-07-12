# Задача 2
# Задача 1.2.

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import random
import datetime
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
my_favorite_songs_3 = random.sample(my_favorite_songs, 3)
print(my_favorite_songs_3)
l = [my_favorite_songs_3[0][1], my_favorite_songs_3[1][1], my_favorite_songs_3[2][1]] # список со временем звучания песен
print(l)
m = int(l[0]) + int(l[1]) + int(l[2]) #  посчитали минуты
s = (l[0] - int(l[0])) * 100 + (l[1] - int(l[1])) * 100 + (l[2] - int(l[2])) * 100 # посчитали секунды
res = m * 60 + s # привели всё к секундам
total_res = round(res // 60 + (res % 60) / 100, 2)  # формула, выведенная эмпирическим путём))
print('Три песни звучат', total_res, 'минут')   
t = str(total_res).split('.')
if len(t[1]) == 1 :  # доп. проверка на корректность
    t[1] += '0'      # последующего вывода времени
total_t = datetime.time(0, int(t[0]), int(t[1]))
print('Три песни звучат', total_t, 'минут')