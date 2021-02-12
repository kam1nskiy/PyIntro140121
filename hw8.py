# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

DEBUG_MODE = True

import string
import random


def create_string(min_limit, max_limit,debug_mode: bool = DEBUG_MODE):
    my_list =[random.choice(string.ascii_lowercase) for i in range(random.randint(min_limit, max_limit))]
    myString = ''.join(my_list)
    if debug_mode:
        print(myString)
    return myString

min_limit = 1
max_limit = 10
hellostring = create_string(1,10)




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

from random import randint
from random import choice

# numbers = ([randint(100, 999) for i in range(5)])
# number =''.join(numbers)


# my_list =([random.choice(string.ascii_lowercase) for i in range(random.randint(min_limit, max_limit))])
# string = ''.join(my_list)

# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
#
# def email(names,domains):
#     name = (random.choice(names))
#     domain = (random.choice(domains))
#     stringa =(''.join(choice(string.ascii_lowercase) for i in range(randint(5, 7))))
#     number = random.randint(100, 1000)
#     mail = (f" {name}.{number}@{stringa}.{domain}")
#     return mail
#
# eemail = email(names, domains)
# print(eemail)


# from random import choice
#
# from string import ascii_letters
#
# print(''.join(choice(ascii_letters) for i in range(12)))

import random
import string


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Alphanum Random string of length", length, "is:", rand_string)


generate_alphanum_random_string(10)