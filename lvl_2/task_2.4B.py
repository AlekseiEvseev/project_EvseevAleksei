# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!' :
        return s[:-1]
    else :
        return s

st = input('Введите строку: ')
print(remove_last_em(st))