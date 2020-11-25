for raw in range(7):
    for col in range(6):
        if col == 0 or raw == 0 and col < 6 or raw == 2 and col < 5 :
            print("*", end="")
        else:
            print(end=" ")
    print("")