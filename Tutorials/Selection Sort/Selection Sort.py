num = [5, 3, 8, 6, 7, 2]
for i in range(5): #len(num)-1
    minpose = i # first itration minpose = 5
    for j in range(i, 6):# 6 = len(num)
        if num[j] < num[minpose]:
            minpose = j
    num[i], num[minpose] = num[minpose], num[i]
print(num)
