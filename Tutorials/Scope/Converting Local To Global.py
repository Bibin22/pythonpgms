a = 10
def fname():
    global a
    a = 15
    print('Inside the function', a)

fname()
print('Outside', a)