def listno(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0]+listno(list[1:])
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = listno(list)
print(sum)