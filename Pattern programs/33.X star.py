i = 0
j = 4
for raw in range(5):
    for col in range(5):
        if raw == i and col == j:
            print("*", end="")
            i = i + 1
            j = j - 1
        elif raw == col:
            print("*", end="")
        else:
            print(end=" ")
    print(" ")