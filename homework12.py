# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
from sys import path

import requests
import csv
import json
import re

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

