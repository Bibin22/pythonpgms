i = 0
j = 5
for raw in range(7):
    for col in range(7):
        if raw == i and col == j:
            print("*", end="")
            i = i + 1
            j = j - 1
        elif raw==0 or raw == 6:
            print("*", end="")
        else:
            print(end=" ")
    print("")