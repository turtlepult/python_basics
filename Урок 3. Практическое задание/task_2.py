class Divide_by_zero(Exception):
    def __init__(self):
        pass


user_number_1 = int(input("Введите первое число: "))
user_number_2 = int(input("Введите второе число: "))


def divide_user_number(num1, num2):
    if (num2 == 0):
        raise Divide_by_zero
    else:
        print(num1 / num2)


try:
    divide_user_number(user_number_1, user_number_2)
except Divide_by_zero:
    print("На ноль делить нельзя!!!")
