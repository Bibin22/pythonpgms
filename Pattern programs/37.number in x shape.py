i = 1
j = 6
for raw in range(1,7):
    for col in range(1,7):
        if raw == col:
            print(col, end="")
        elif raw ==i and col == j:
            print(raw, end="")
            i = i+1
            j = j-1

        else:
            print(end=" ")
    print(" ")