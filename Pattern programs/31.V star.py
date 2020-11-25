i = 0
j = 6
for raw in range(4):
    for col in range(7):
        if raw == col:
            print("*", end="")
        elif raw == i and col == j:
            print("*", end="")
            i = i +1
            j = j - 1
        else:
            print(end=" ")
    print("")