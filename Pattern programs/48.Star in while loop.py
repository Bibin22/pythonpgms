num = int(input("Enter a number"))
i = 0
while i < num:
    j = i + 1
    while j > 0:
        print("* ", end="")
        j = j - 1
    i = i + 1
    print('')