input_value_mn = [int(x) for x in input("aksjdbas: ").split()]
m = input_value_mn[0]
n = input_value_mn[1]

set_1 = set([int(x) for x in input("123213: ").split()])
set_2 = set([int(x) for x in input("1231232: ").split()])
while len(set_1) > m or len(set_2) > n:
    print("Вы ввели больше количество элементов, чем задали:")
    set_1 = set([int(x) for x in input("123213: ").split()])
    set_2 = set([int(x) for x in input("1231232: ").split()])
print(set_1)
print(set_2)
res_set = list(set_1 & set_2)
res_set.sort()
for i in res_set:
    print(i, end=' ')
