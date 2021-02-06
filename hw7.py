# from random import randint
# lst = [randint(0, 100) for i in range(20)]
# print(lst)
#######################################################################
# для int
# from random import uniform as ru
# triangle1 = {x:(ru(-10.0, 10), ru(-10.0, 10)) for x in ['A','B', 'C']}
# print (triangle1)
# #для float
# from random import randint as rndint
# triangle2 = {x:(rndint(-10.0, 10), rndint(-10.0, 10)) for x in ['A','B', 'C']}
# print (triangle2)
###############################################################################
# my_str = input('Введите строку:')
# def func (my_str) :
#     print ("***",my_str,"***")
# func(my_str)
###############################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# persons=[{"name": "Василь", "age": 100}, {"name": "Петроу", "age": 100} ,{"name": "Іван", "age": 100}]
# ages=[value["age"] for value in persons]
# for value in persons:
#     if value["age"]==min(ages):
#         print(value["name"])
###############################################################################
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# persons=[{"name": "Василь", "age": 100}, {"name": "Петроу", "age": 110} ,{"name": "Іван", "age": 111}]
# names=[len(value["name"]) for value in persons]
# for value in persons:
#     if len(value["name"])==max(names):
#         print(value["name"])
###############################################################################
# # в) Посчитать среднее количество лет всех людей из списка.
# persons=[{"name": "Василь", "age": 100}, {"name": "Петроу", "age": 110} ,{"name": "Іван", "age": 111}]
# ages=[value["age"] for value in persons]
# avarage=sum(ages)/len(ages)
# print(avarage)
# Красивое решение 4го задание через collections
# from collections import defaultdict
#
# persons = [
#     {"name": "Sam", "age": 10},
#     {"name": "Jackky", "age": 10},
#     {"name": "Mal", "age": 12},
#     {"name": "Ray", "age": 97}
# ]
#
# age_by_names = defaultdict(list)
# len_name_by_names = defaultdict(list)
# ages = []
#
# for p in persons:
#     name = p['name']
#     age = p['age']
#     age_by_names[age].append(name)
#     len_name_by_names[len(name)].append(name)
#     ages.append(age)
#
# min_age = min(age_by_names)
# print('min_age:', *age_by_names[min_age])
#
# max_len_name = max(len_name_by_names)
# print('max_len_name:', *len_name_by_names[max_len_name])
#
# print('average:', sum(ages) // len(ages))
###############################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
my_dict_1 = {'василь':'кіт','петро':'молодець','іван':'пан'}
my_dict_2 = {'василь':'пес','петро':'холодець'}
keys_a = set(my_dict_1.keys())
keys_b = set(my_dict_2.keys())
intersection = list(keys_a & keys_b)
print(intersection)
###############################################################################
# # б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
diff=[key for key in keys_a.difference(keys_b)]
# print(diff,type(diff))
###############################################################################
# # в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict={key:item for key,item in my_dict_1.items() if key in diff}
print(new_dict)
###############################################################################
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# def mergeDict(dict1, dict2):
#     for k, v in dict2.items():
#         if dict1.get(k):
#             dict1[k] = [dict1[k], v]
#         else:
#             dict1[k] = v
#     return dict1
#
# my_dict_1 = {'василь':'кіт','петро':'молодець','іван':'пан'}
# my_dict_2 = {'василь':'пес','петро':'холодець'}
#
# my_dict_3 = mergeDict(my_dict_1, my_dict_2)
#
# print(my_dict_3)






