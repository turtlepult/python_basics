list_main = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_num = int(input("Введите минимальное значение: "))
max_num = int(input("Введите максимальное значение: "))

for i in range(len(list_main)):
    if min_num <= list_main[i] <= max_num:
        print(i)
