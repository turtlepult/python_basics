# Узнайте у пользователя целое положительное число n. Найдите сумму чисел n + nn + nnn.
user_number_input = int(input('Enter a positive integer: '))
int_to_str = str(user_number_input)
castom_number = int_to_str + int_to_str
castom_number1 = int_to_str + int_to_str + int_to_str
print(f"n+nn+nnn = {user_number_input + int(castom_number) + int(castom_number1)}")
