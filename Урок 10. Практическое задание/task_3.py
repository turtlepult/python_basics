"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
main_list = ["attribute", "класс", "функция", "type"]
for i in main_list:

    try:
        print(i, bytes(i, encoding='ASCII'))
    except UnicodeEncodeError:
        print(f"\"{i}\" невозможно преобразовать")
    print()
