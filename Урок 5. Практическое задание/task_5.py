def ascii(i=32, count=0):
    if i > 127:
        return
    else:
        if count == 10:
            print()
            count = 0
        else:
            print(f"{i} - {chr(i)}", end="")
        i += 1
        count += 1
        return ascii(i, count)


ascii()
