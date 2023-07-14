# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    lst, lst2 = s.split(), []  # создаём списки
    for i in range(len(lst)) :
        if lst[i].count('!') != 1 :  # если элемент списка lst не содержит ровно один восклицательный знак,
            lst2.append(lst[i])      # то добавляем его в конец списка lst2 
    return lst2        

st = input('Введите строку: ')
print(*remove_word_with_one_em(st))  # распаковываем список и выводим на печать
