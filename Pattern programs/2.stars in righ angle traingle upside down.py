num = int(input("Enter a number"))
for i in range(num+1, 1, -1):
    for j in range(1, i):
        print("* ", end=" ")
    print()