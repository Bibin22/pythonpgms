l1 = [1, 3, 6, 9, 8]
l2 =[2, 4, 5, 7]
i1 = iter(l1)
i2 = iter(l2)
i3 = sorted(list(i1) + list(i2))
print(i3)
