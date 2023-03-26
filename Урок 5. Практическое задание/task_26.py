def degree(a, b, res=1, i=1):
    if b<i:
        print(res)
        return
    else:
        res *= a
        i += 1
        return degree(a,b,res,i)

a = int(input("веддите число основание: "))
b = int(input("веддите число показатель степени: "))
degree(a, b)
