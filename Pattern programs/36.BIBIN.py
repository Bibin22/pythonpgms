lst1b = [[" " for i in range(7)] for j in range(7)]
lst2i = [[" " for i in range(7)]for j in range(7)]
lst3b = [[" " for i in range(7)] for j in range(7)]
lst4i = [[" " for i in range(7)]for j in range(7)]
lst5n = [[" " for i in range(7)]for j in range(7)]

#B
for raw in range(7):
    for col in range(7):
        if (col ==0) or ((raw ==0 or raw== 3 or raw == 6)and col > 0 and col <6) or ((col == 6)and raw!=0 and raw!=3 and raw!=6):
            lst1b[raw][col] = "*"

#I
for raw in range(7):
    for col in range(7):
        if raw == 0 or raw == 6 or col == 3:
            lst2i[raw][col] = "*"




#B
for raw in range(7):
    for col in range(7):
        if (col ==0) or ((raw ==0 or raw== 3 or raw == 6)and col > 0 and col <6) or ((col == 6)and raw!=0 and raw!=3 and raw!=6):
            lst3b[raw][col] = "*"

#I
for raw in range(7):
    for col in range(7):
        if raw == 0 or raw == 6 or col == 3:
            lst4i[raw][col] = "*"


#N
for raw in range(7):
    for col in range(7):
        if col == 0 or col == 6 or raw == col:
            lst5n[raw][col] = "*"


for i in range(7):
    for j in range(7):
        print(lst1b[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(lst2i[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(lst3b[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(lst4i[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(lst5n[i][j], end=" ")
    print(" ")

