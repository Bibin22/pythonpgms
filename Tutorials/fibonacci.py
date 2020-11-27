
a = 0
b = 1
n = int(input("Enter the Limit"))
if n == 1:
    print(a)
elif n < 0:
    print("Enter number Greater than Zero")
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
