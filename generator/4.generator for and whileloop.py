def gen():
    n = 0
    while n <= 10:
        sq = n*n
        yield sq
        n = n + 1
val = gen()
for i in val:
    print(i)