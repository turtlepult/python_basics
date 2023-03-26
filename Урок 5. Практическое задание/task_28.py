def sum(a, b):
    if b == 0:
        print(a)
        return
    else:
        a += 1
        b -= 1
        return sum(a, b)

a = int(input("a: "))
b = int(input("b: "))
sum(a, b)
