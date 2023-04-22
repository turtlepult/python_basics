"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
main_list = ["разработка", "администрирование", "protocol", "standard"]
for i in main_list:
    text_bytes = i.encode(encoding='utf-8')
    print(text_bytes)
    print(text_bytes.decode(encoding='utf-8'))
    print()



