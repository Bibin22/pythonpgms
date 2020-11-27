num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
even= list(filter(lambda n : n % 2 == 0, num))
print(even)
double = list(map(lambda n: n * 2, even))
print(double)
