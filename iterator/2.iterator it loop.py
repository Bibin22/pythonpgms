num = [1, 2, 3, 4, 5]
it = iter(num)
print(it.__next__())#output 1
for i in num:
    print(i)#output 1-5


# in this it will print 1 as output of 'print(it.next())' and will print 1,2,3,4,5 as output of the for loop and
#final output be like 1, 1, 2, 3, 4, 5,  so theris two 1's
#check 3.iterator it loop.py