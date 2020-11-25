num = [1, 2, 3, 4, 5]
it = iter(num)
print(next(it))#output 1
print(it.__next__())#output 2
