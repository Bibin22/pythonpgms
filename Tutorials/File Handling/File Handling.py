f = open('mydata')
print(f.readline())
print(f.readline(4))

f1 = open('abc', 'a')
f1.write('my name is Bibin')

for data in f:
    f1.write(data)