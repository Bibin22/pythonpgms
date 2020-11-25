def gen():
    for i in range(1, 11):
        yield i

val = gen()
for i in val:
    print(i)