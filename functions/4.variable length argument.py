def add(a, *b):
    print('a =', a)
    print('b =', b)

add(10, 20, 30, 40)


print("EXAMPLE FOR VARIABLE LENGTH ARGUMENT")

def sum (*b):
    print('b = ', b)
    c = 0
    for i in b:
        c = c + i
    print(c)

sum(12,34, 56, 78)