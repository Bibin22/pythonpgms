for raw in range(7):
    for col in range(7):
        if raw == 0 or col == 3 and raw!=0:
            print("*",end="")
        else:
            print(end=" ")
    print("")