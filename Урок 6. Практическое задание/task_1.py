first_elem = int(input("Введите первый элемент: "))
diff = int(input("Введите шаг прогресии: "))
n = int(input("Введите количество элементов: "))
for i in range(n):
    print(first_elem + i * diff)
