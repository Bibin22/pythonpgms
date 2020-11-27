def difference(n):
    if n > 17:
        return 2*(n-17)

    else:
       return 17-n


i = int(input("Enter a number"))
res = difference(i)
print(res)