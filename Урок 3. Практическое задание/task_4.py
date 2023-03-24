"""
def my_func (var_1, var_2, var_3):
    fakearr = [var_1, var_2, var_3]
    fakearr.sort()
    print(fakearr[-1]+fakearr[-2])

my_func(987, 546, 654)
"""
def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')

my_func(654, 984, 648)