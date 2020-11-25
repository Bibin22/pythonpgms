def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

val = gen()
for i in val:
    print(i)
