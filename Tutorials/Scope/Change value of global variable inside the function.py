a = 10
def fname():
    a = 9
    print('Local variable a =', a)
    globals()['a'] = 15

fname()
print('outside a',a)