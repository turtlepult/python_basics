""""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
user_input_time = int(input('enter the time in seconds: '))
time_in_hours = user_input_time / 3600
time_in_minutes = user_input_time / 60
print(f"Время в формате ч:м:с - {time_in_hours} : {time_in_minutes} : {user_input_time}")
