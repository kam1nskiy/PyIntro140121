# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


import requests
import csv
import json
import re
from os import path

def get_quotes(quantity, filename=r"C:\Users\kaminskyi\PycharmProjects\PyIntro140121\test.csv"):

    quotes = set()
    while len(quotes) < quantity:
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": 1,
                  "lang": "ru"}
        responce = requests.get(url, params=params)
        quote = responce.json()
        q = (quote["quoteText"], quote["quoteAuthor"], quote["quoteLink"])
        if quote["quoteAuthor"] != "":
            quotes.add(q)
    result = sorted(list(quotes), key=lambda quotes: quotes[1])
    # print(result)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ["Author", "Quote", "URL"]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(result)


get_quotes(10)


def read_authors(path=r"C:\Users\kaminskyi\PycharmProjects\PyIntro140121\authors.txt"):
    with open(path, "r") as text_file:
        complete_list = text_file.readlines()
        authors_list = []
        for line in complete_list:
            if "'s" in line:
                authors_list.append(line)
    return authors_list


def create_dict_authors(list_authors):
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    dict_list = []
    for line in list_authors:
        index_start_name = line.find("- ") + 2
        index_end_name = line.find("'s")
        name = line[index_start_name:index_end_name]
        pattern = r"[0-9]{1,2}"
        result = re.findall(pattern, line)
        day = result[0]
        year = f"{result[1]}{result[2]}"
        month = months[line.split()[1]]
        dict_list.append({"name": name, "date": f'{day}/{month}/{year}'})
    return dict_list


def write_json(authors_dicts_list, json_authors=r"C:\Users\kaminskyi\PycharmProjects\PyIntro140121\authors.json"):
    with open(path.join(json_authors), "w") as json_file:
        json.dump(authors_dicts_list, json_file, indent=1)
    return None


# get_quotes(10)
# list_of_artist = read_authors()
# print(list_of_artist)
authors_dict = create_dict_authors(read_authors())
print(authors_dict)
write_json(authors_dict)