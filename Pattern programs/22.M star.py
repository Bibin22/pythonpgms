for raw in range(7):
    for col in range(7):
        if col == 0 or col == 6 or raw == col and col > 0 and col < 4 or raw == 2 and col == 3 or raw == 1 and col == 4:
            print("*", end="")
        else:
            print(end=" ")
    print("")