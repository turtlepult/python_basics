user_name = input("Введите ваше имя и фамилию через пробел: ")
birth_day = input("Введите ваш год рождения: ")
user_city = input("Введите ваш город проживания: ")
user_email = input("введите ваш email: ")
phone_number = input("Введите ваш номер телефона: ")


def information_by_people(name, birthday, city, email, phonenumber):

    print(f"{name} {birthday} года рождения, проживает в городе {city}, "
          f"email: {email}, телефон: {phonenumber}")


information_by_people(name =user_name , birthday=birth_day , city=user_city,
                      email=user_email, phonenumber=phone_number)
