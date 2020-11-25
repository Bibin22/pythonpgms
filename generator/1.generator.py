def gen():
    yield 1
val = gen()
print(val.__next__())