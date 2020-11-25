num = int(input("enter a number"))
num1 = num
for i in range(0, num):
    for j in range(0, num):
        print(end=" ")
    num = num - 1
    for k in range(0, i+1):
        print("* ", end=" ")
    print(" ")

for i in range(num1, 0, -1):
    for j in range(0, num1-i):
        print(end=" ")

    for k in range(0, i):
        print("* ", end="")
    print(" ")