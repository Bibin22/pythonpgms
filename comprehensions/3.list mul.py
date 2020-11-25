A = ['a', 'b', 'c']
B = [1, 2, 3, 4]
AxB = [(x, y) for x in A for y in B]
for i in AxB:
    print(i)