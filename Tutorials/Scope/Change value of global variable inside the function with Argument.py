a = '' #value of Global variable a is not defined  (or we can define a value its not a problem
def fname(g):
    a = 9 #Local variable a
    print('Local variable a =', a)
    globals()['a'] = g

gl = 15
fname(gl)
print('Outside / Global variable  a =', a)