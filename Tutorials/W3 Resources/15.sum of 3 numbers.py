def sum(a, b, c):
    if a == b == c:
        return (a + b + c) *3
    else:
        return a + b + c



a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
res = sum(a, b, c)
print(res)