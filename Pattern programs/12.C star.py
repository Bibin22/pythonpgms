for raw in range(7):
    for col in range(6):
        if((col == 0)and raw != 0 and raw!= 6)or ((raw ==0 or raw == 6)and(col > 0 )):
            print("*", end="")
        else:
            print(end=" ")
    print()