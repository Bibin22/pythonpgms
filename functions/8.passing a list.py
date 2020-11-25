def search(list, n):
    p = 0
    for i in list:
        if n == i:
            print(n,'found at position ', p)
        else:
            (n,'not found')
        p = p + 1


search([1, 2, 5, 6, 3, 8, 9, 10], 5)