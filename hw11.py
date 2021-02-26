import json
import re


# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def read_json_file(file_path):
    with open(file_path, encoding="utf-8") as json_doc:
        content = json.load(json_doc)
    return content


data = read_json_file(r"C:\Users\kaminskyi\PycharmProjects\PyIntro140121\hw11.json")

print(type(data))


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).


def sort_by_surname(names_dict):
  return names_dict['name'].split()[-1]


data = sorted(data, key=sort_by_surname)
print(data)



# 3. Написать функцию сортировки по дате смерти из поля "years".
def sort_years(names_dict):
    if names_dict["years"].endswith("BC."):
        dates = r"[0-9]+"
        death_year = int(re.findall(dates, names_dict["years"])[-1]) * -1
    else:
        dates = r"[0-9]+"
        death_year = int(re.findall(dates, names_dict["years"])[-1])
    return death_year


sorted_years = sorted(data, key=sort_years)
print(sorted_years)


# 4. Написать функцию сортировки по количеству слов в поле "text"
def sort_len(names_dict):
    text_len = len(names_dict["text"])
    return text_len


sorted_len = sorted(data, key=sort_len)
print(sorted_len)
