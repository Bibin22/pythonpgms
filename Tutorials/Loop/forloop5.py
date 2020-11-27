c = 0
n = int(input("Enter the Limit"))
for i in range(n):
    if i % 2 == 0:
        print(i)
        c = c + 1
    elif i % 2 != 0:
        print(i)
        c = c + 1

print("Even Count =", c)
print("Odd Count =", c)

