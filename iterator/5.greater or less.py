list = [1, 2, 3, -1, -3, -2]
li =[]
l2 = []
t = iter(list)
for i in t:
    if i > 0:
        li.append(i)
    else:
        l2.append(i)

print(li)
print(l2)



