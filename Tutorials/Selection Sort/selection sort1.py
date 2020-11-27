list = [5, 4, 3, 2, 1]
for i in range(len(list)-1):
    minpose = 1
    for j in range(i, len(list)):
        if list[j] < list[minpose]:
            minpose = j

    list[i], list[minpose] = list[minpose], list[i]
print(list)