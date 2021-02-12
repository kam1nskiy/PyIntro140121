import string
import random


def create_random_str(rand_flag=False):
    alphabet = string.ascii_lowercase
    count = random.randint(1, 10) if rand_flag else 2
    return alphabet * count


def create_spaces(rand_str):
    index = 0
    rand_str_to_list = list(rand_str)
    condition = True
    while condition:
        step = random.randint(1, 10)
        index += step
        if index < len(rand_str):
            rand_str_to_list[index] = " "
        else:
            condition = False
    rand_str = "".join(rand_str_to_list)
    return rand_str


def modify_word(word, comma_percentage=0.2):
    if random.random() < comma_percentage:
        word = word.capitalize()
    return word


def modify_str(rand_str):
    rand_str_split = rand_str.split()
    result = []
    for word in rand_str_split:
        word = modify_word(word)
        result.append(word)
    return " ".join(result)


rand_str = create_random_str(True)
rand_str = create_spaces(rand_str)
rand_str = modify_str(rand_str)
print(rand_str)