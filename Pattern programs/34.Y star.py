for raw in range(5):
    for col in range(5):
        if (col == 2 and raw>1 ) or (raw == col and col < 2) or (raw == 0 and col == 4)or(raw == 1 and col == 3):
            print("*", end="")
        else:
            print(end=" ")
    print("") 