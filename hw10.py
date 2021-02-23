import json
import csv


# 1. Написать функцию read_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) считывает и возвращает данные из файла.
# Для csv использовать reader.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"


def read_txt(file_path):
    with open(file_path, 'r') as txt_file:
        content = txt_file.read()
    return content


def read_json(file_path):
    with open(file_path, 'r') as json_file:
        content = json.load(json_file)
    return content


def read_csv(file_path):
    with open(file_path, 'r', encoding="utf-8") as csv_file:
        content = []
        reader = csv.reader(csv_file)
        for row in reader:
            content.append(row)
    return content

def read_file(file_path):
    extension = file_path.rsplit('.', 1)[-1]
    if extension == 'txt':
        res = read_txt(file_path)
    elif extension == 'json':
        res = read_json(file_path)
    elif extension == 'csv':
        res = read_csv(file_path)
    else:
        res = "Unsupported file format"
    return res


print(read_file(r'C:\Users\kaminskyi\PycharmProjects\PyIntro140121\data.json'))

# 2. Написать функцию write_file которая принимает два параметра - полный путь к файлу и данные.
# В зависимости от расширения файла (txt, csv, json) записывает данные в данный файл.
# Для csv использовать DictWriter.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"




data = [{"Name": "Emma", "Age": 13, "Hair_color": "orange"}]


def write_file(file_path, data):
    if file_path.endswith(".txt"):
        with open(file_path, "w") as txt_doc:
            txt_doc.writelines(data)

    elif file_path.endswith(".json"):
        with open(file_path, "w") as json_doc:
            json.dump(data, json_doc, indent=4)

    elif file_path.endswith(".csv"):
        with open(file_path, "w") as csv_doc:
            field_name_row = data[0]
            fieldnames = field_name_row.keys()
            csv_writer = csv.DictWriter(csv_doc, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    else:
        print("Unsupported file format!")



write_file(r'C:\Users\kaminskyi\PycharmProjects\PyIntro140121\test.csv', data)
