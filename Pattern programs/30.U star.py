for raw in range(7):
    for col in range(7):
        if ((col == 0 or col == 6) and raw!= 6) or ((raw == 6) and col > 0 and col < 6):
            print("*", end="")
        else:
            print(end=" ")
    print("")