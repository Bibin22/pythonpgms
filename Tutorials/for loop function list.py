
def listfunction(lst):
    odd = 0
    even = 0

    for i in lst:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd



list1 = []
limit = int(input('Enter the Limit'))
for i in range(limit):
    list1.append(int(input("Enter List values")))
print(list1)

even, odd = listfunction(list1)
print('Evenn {} and Odd {} '.format(even, odd))




