def parity_counter(num, count):
    last_number = num % 10
    num = num // 10
    if last_number % 2 == 0:
        count[1] += 1
    elif last_number % 2 != 0:
        count[0] += 1
    if num == 0:
        print(f"[нечетные, четные]{count}")
        return
    else:
        return parity_counter(num, count)

counter = [0] * 2
user_number = int(input("Введите число:"))
parity_counter(user_number, counter)
