num = [1, 2, 3, 4, 5]
it = iter(num)
print(it.__next__())#output 1
for i in it:
    print(i)

# in this it will print 1 as output of 'print(it.next())' but the output 1 of 'print(it.next()) will ignore when execute the loop
#final output be like 1, 2, 3, 4, 5,  so there is no two 1's