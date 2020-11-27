def count(list):
    c = 0
    for i in list:
        if i == 4:
            c = c + 1

    return c


list=[1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
c = count(list)
print(c)