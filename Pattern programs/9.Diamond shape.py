def pyramid(num):
    for i in range(num):
        print(" "*(num-i-1), "* "*(i+1))
    for j in range(num-1, 0, -1):
        print(" "*(num-j), "* "*(j))

n = int(input("Enter a number"))
pyramid(n)