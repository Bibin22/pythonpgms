def genarator():
    n = 1
    while n <= 10:
        yield n
       # sq = n * n
       # yield sq
        n = n + 1


values = genarator()
for i in values:
    print(i)