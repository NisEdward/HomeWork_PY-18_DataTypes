import json
import xml.etree.ElementTree as ET
from operator import itemgetter


# Функция формирования списка слов длинною более 6 символов, подсчета количества (частоты) слов, вывод ТОП-10 слов
def new_list_function(string):
    i = 0
    new_list = list()
    while i < len(string):
        if len(string[i]) > 6:
            new_list.append(string[i])
        i += 1

    dict_new = dict()
    for word in new_list:
        i = 0
        count = 0
        while i < len(new_list):
            if word == new_list[i]:
                count += 1
            i += 1
        dict_new[word] = count

    sorted_new_list = sorted(dict_new.items(), key=itemgetter(1), reverse=True)
    print(sorted_new_list)

    i = 0
    while i < 9:
        print(sorted_new_list[i][0])
        i += 1


# Работа с файлом в формате Json
with open("newsafr.json", encoding="Utf-8") as json_file:
    news = json.load(json_file)
    i = 0
    new_string = ""
    while i < len(news["rss"]["channel"]["items"]):
        string_description = news["rss"]["channel"]["items"][i]["description"]
        string_title = news["rss"]["channel"]["items"][i]["title"]
        new_string += " " + string_description + " " + string_title
        i += 1
    new_string_list = new_string.strip().split(" ")
    new_string_list = sorted(new_string_list)

# Вызов функции для формирования нового списка и формирования ТОП-10
print("\t\t Обработка файла в формате JSON и вывод ТОП-10 часто встречающихся слов длиннее 6 символов:")
new_string_list = new_list_function(new_string_list)

# Работа с файлом в формате Xml
tree = ET.parse("newsafr.xml")
titles = tree.findall("channel/item/title")
descriptions = tree.findall("channel/item/description")
new_string = ""
for title in titles:
    new_string += " " + title.text
for description in descriptions:
    new_string += " " + description.text
new_string_list = new_string.strip().split(" ")
new_string_list = sorted(new_string_list)
# Вызов функции для формирования нового списка и формирования ТОП-10
print("\t\t Обработка файла в формате XML и вывод ТОП-10 часто встречающихся слов длиннее 6 символов:")
new_string_list = new_list_function(new_string_list)


