
import random as rnd
from random import randint
from random import choice
import string




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


print(random_string(5, 10))
