# Найдите сумму цифр трехзначного числа.
main_number = 51562654
str_main_number = str(main_number)
i = 0
sum_numbers = 0
while (i < len(str_main_number)):
    temp = int(str_main_number[i])
    sum_numbers += temp
    i = i + 1

print(sum_numbers)
