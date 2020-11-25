for raw in range(6):
    for col in range(6):
        if col == 2 and raw!=0 and raw!=5 or raw==0 or raw== 5:
            print("*", end="")
        else:
            print(end=" ")
    print("")