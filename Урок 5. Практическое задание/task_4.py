def revers_number(num, rev):
    if num == 0:
        print(rev)
        return
    else:
        rev += str(num % 10)
        return revers_number(num // 10, rev)

user_number = int(input("Введите число: "))
rev = ""
revers_number(user_number, rev)
