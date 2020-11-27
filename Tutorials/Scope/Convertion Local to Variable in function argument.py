a = 10
def fname(b):
    global a
    a = b
    print("Iside the function", a)

n = 78
fname(n)
print('outside', a)