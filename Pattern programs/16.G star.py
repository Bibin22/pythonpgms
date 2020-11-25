for raw in range(7):
    for col in range(8):
        if col == 0 or raw == 6 and col < 4  or raw == 3 and col > 3 and col < 8 or col == 5 and raw!=0 and raw!=1 and raw!=2 or col == 7 and raw!=0 and raw!=1 and raw!=2 or raw == 0 and col > 0 and col < 8 :
            print("*" , end="")
        else:
            print(end=" ")
    print(" ")