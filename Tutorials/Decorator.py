def div(a, b):
    print(a / b)
    print('a =', a, 'b=', b)
def smartdiv(fun):

    def inner(a, b):
        print(' a before swap =', a, 'b before swap =', b)
        if a < b:
            a, b = b, a
            print('inner a=', a, 'inner b =', b)
        return fun(a, b)
    return inner


div1 = smartdiv(div)

 