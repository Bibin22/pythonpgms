for raw in range(7):
    for col in range(7):
        if col == 0 and raw!=0 or ((raw==0 or raw==3) and col > 0 and col < 6)or (raw ==1 and col ==6 or raw ==2 and col ==6) :
            print("*",end="")
        else:
            print(end=" ")
    print("")