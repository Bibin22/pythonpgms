n1 = int(input("Enter a Number"))
n2 = int(input("Enter second number"))
if n1 < n2:
    n1, n2 = n2, n1
    print(n1/n2)
else:
    print(n1/n2)