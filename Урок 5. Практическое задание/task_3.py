from random import randint


def game_random(rand, count=1):
    user_guess = int(input(f"Попытка {count}/10 введите число: "))
    if user_guess == rand:
        print("Поздравляем вы угадали!!!!!")
        return
    else:
        count += 1
        if count == 11:
            print(f"Игра окончена, загаданное число {rand}")
        else:
            if user_guess > rand:
                print("Вы ввели число больше загаданного!")
            else:
                print("Вы ввели число меньше загаданного!")
            return game_random(rand, count)


random_number = randint(0, 100)
game_random(random_number)
