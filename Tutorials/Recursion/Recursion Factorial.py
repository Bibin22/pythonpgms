def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)

f = int(input("Enter Number"))
result = fact(f)
print(result)