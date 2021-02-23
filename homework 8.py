import random as rnd
from random import randint
from random import choice
import string


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

num_min = 100
num_max = 999
symb_min = 5
symb_max = 7


def email(names, domains):
    name = (rnd.choice(names))
    domain = (rnd.choice(domains))
    stringa = (''.join(choice(string.ascii_lowercase) for i in range(randint(symb_min, symb_max))))
    number = rnd.randint(num_min, num_max)
    mail = (f" {name}.{number}@{stringa}.{domain}")
    return mail


eemail = email(names, domains)
print(eemail)

# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

def len_random(min_limit, max_limit):
    result = "".join(choice(ascii_letters) for _ in range(randint(min_limit, max_limit)))
    return result


print(len_random(5, 10))
def transform_text(text):
    index = 0
    text = list(text)
    while index + 10 < len(text):
        possible_symbols = [", ", " ", "\n", " " + str(randint(1, 50)) + " "]
        space_point = randint(2, 10)
        index += space_point
        text[index] = choice(possible_symbols)
    text.append(".")
    text = "".join(text)
    text = text.title() # если только первая буква большая, то capitalize, если хотим чтобы некоторые буквы были маленькими - используем функцию ниже
    return text


# print(transform_text(len_random(100,140)))

def add_lower_case(text):  # опционально, если я хочу чтобы случайным образом буквы в начале слова были маленькими / большими
    i = 0
    text = list(text)
    while i + 3 < len(text):
        upper_point = randint(1,3)
        i += upper_point
        text[i] = text[i].lower()
    return "".join(text)


print(add_lower_case(transform_text(len_random(150,200))))