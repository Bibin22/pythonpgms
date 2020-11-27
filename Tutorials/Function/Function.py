def add(x, y):
    c = x + y
    d = x - y
    return c, d

a = int(input("Enter Number"))
b = int(input("Enter Number"))
result1, result2 = add(a, b)
print(result2, result1)