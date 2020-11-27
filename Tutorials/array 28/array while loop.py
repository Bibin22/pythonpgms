import array as arr
a = arr.array('i', [1, 5, 3, 4, 5])
b = 1
while b < a[3]:
    print(a[b])
    b = b + 1
print('loop finished')