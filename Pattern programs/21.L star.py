for raw in range(7):
    for col in range(7):
        if col == 0 or raw == 6:
            print("*",end="")
        else:
            print(end=" ")
    print("")