def even(n):
    return n % 2 == 0
num = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 12, 13,]
evn = list(filter(even, num))
print(evn)