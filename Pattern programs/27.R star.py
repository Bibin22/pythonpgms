for raw in range(7):
    for col in range(7):
        if (col == 0) or (raw == col+2) or ((raw == 0 or raw ==2)and col<5 )or (raw ==   1 and col == 6):
            print("*", end="")
        else:
            print(end=" ")
    print("")