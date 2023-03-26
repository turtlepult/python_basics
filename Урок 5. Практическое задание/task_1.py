def calc():
    operation = input("Введите операцию(+, -, *, / или 0 для выхода из программы): ")
    if operation == "+":
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        print(f"Ваш результат: {num_1 + num_2}")
        return calc()
    elif operation == "-":
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        print(f"Ваш результат: {num_1 - num_2}")
        return calc()
    elif operation == "*":
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        print(f"Ваш результат: {num_1 * num_2}")
        return calc()
    elif operation == "/":
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        if num_2 == 0:
            print("на ноль делить нельзя!!!")
            return calc()
        else:
            print(f"Ваш результат: {num_1 / num_2}")
    elif operation == "0":
        return
    else:
        print("Вы ввели не верную операцию!!!")
        return calc()

calc()
