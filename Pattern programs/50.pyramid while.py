n = int(input("Enter a number"))
i = 0
while i < n:
    s = n - i - 1
    while s > 0:
        print(" ", end="")
        s = s - 1
    j = i + 1
    while j > 0:
        print("* ",end="")
        j = j - 1
    i = i + 1
    print('')
