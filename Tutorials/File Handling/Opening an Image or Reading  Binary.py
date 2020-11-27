f = open('IMG_20191117_081717_233.jpg', 'rb')
#print(f.read())

f1 = open('myimage.jpg', 'wb')
for i in f:
    f1.write(i)