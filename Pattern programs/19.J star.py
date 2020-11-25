for raw in range(6):
    for col in range(6):
        if col == 3 and raw!=0 and raw!=5 or raw == 0 and col >= 0 and col < 6 or raw == 5 and col >= 0 and col < 3:
            print("*", end="")
        else:
            print(end=" ")

    print("")