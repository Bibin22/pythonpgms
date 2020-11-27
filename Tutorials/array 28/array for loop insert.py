import array as arr
a = arr.array('i')
print("Enter Array Values")
for i in range(10):
    a.append(int(input("Enter elements")))
print(a)