a = 10
def fname():
    a = 9
    print(' a inside the function', a)
    #globals()['a'] = 15  # NOw the value of Global variable change to 15
    x = globals()['a']
    print('X acces the global variable a inside the function now x = ', x)


fname()
print('Outside', a)