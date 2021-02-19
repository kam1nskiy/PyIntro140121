import random
import json
import string


# 1. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

def get_surname(path, position=1):
    names = []
    with open(path) as file:
        for line in file:
            line = line.strip().split("\t")
            names.append(line[position])
    return names


surnames = get_surname('/Users/kaminskyi/PycharmProjects/PyIntro140121/names.txt', 1)
print(surnames)


# 2. Создать функцию для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

# создаем строку из случайных букв
def random_string(min_limit, max_limit):
    chars = string.ascii_letters
    str_range = random.randint(min_limit, max_limit)
    return ''.join(random.choice(chars) for i in range(str_range))


# создаем рандомное значение ключа типа инта,флоата или bool
def get_random_value(type, value_rules):
    if type == "int":
        val = random.randint(value_rules[type]["min"], value_rules[type]["max"])
    elif type == "float":
        val = random.random()
    elif type == "bool":
        val = random.choice(value_rules[type])
    else:
        return "unknown error"
    return val


json_key_len = 5
keys_min = 5
keys_max = 20
value_rules = {"float": {"min": 0, "max": 1}, "int": {"min": -100, "max": 100}, "bool": [True, False]}
keys = random.randint(keys_min, keys_max)
k: int
random_values = {random_string(json_key_len, json_key_len).lower():
                     get_random_value(random.choice(["bool", "float", "int"]), value_rules) for k in
                 range(keys)}
# print(random_values)
data = json.dumps(random_values)
print(data)


# 3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
# Cгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.

def generate_and_write_json(file_path):
    with open(file_path, 'w') as file:
        loaded = json.loads(data)
        json.dump(loaded, file, indent=2)


generate_and_write_json('/Users/kaminskyi/PycharmProjects/PyIntro140121/data.json')
