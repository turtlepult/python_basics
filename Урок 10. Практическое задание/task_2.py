"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
main_list = ["class", "function", "method"]
for i in main_list:
    temp_list = []
    temp_list.append(bytes(i, "utf-8"))

    print(temp_list, len(bytes(i, "utf-8")))



