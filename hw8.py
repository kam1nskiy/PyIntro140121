
import random as rnd
from random import randint
from random import choice
import string

from string import ascii_letters



# 1. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
#
# Пример:

# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com



names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

num_min = 100
num_max = 999
min_limit = 5
max_limit = 7


def email(names, domains):
    name = (rnd.choice(names))
    domain = (rnd.choice(domains))
    stringa = (''.join(choice(string.ascii_lowercase) for i in range(randint(min_limit, max_limit))))
    number = rnd.randint(num_min, num_max)
    mail = (f" {name}.{number}@{stringa}.{domain}")
    return mail


eemail = email(names, domains)
print(eemail)


# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

def random_string(min_limit, max_limit):
    result = "".join(choice(ascii_letters) for _ in range(randint(min_limit, max_limit)))
    return result


print(random_string(10, 50))


# 3. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 2 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.


def modify_text(rnd_str):
    i = 0
    rnd_str = list(rnd_str)
    while i + 10 < len(rnd_str):
        numb =" " + str(randint(1, 50)) + " "
        symb = [", ", " ", "\n",numb ]
        space = randint(1, 10)
        i += space
        rnd_str[i] = choice(symb)
    rnd_str.append(".")
    rnd_str = "".join(rnd_str)
    rnd_str = rnd_str.title()
    return rnd_str



def lowercase(rnd_str):
    i = 0
    rnd_str = list(rnd_str)
    while i + 3 < len(rnd_str):
        uppercase = randint(1,3)
        i += uppercase
        rnd_str[i] = rnd_str[i].lower()
    return "".join(rnd_str)


print(lowercase(modify_text(random_string(150,500))))


