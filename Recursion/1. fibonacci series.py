def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return (fib(n-1)+fib(n-2))
n = int(input("Enter a numnber"))
f = fib(n)
print(f)