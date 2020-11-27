lst =[]
n = int(input("Enter the range"))
for i in range(n):
    lst.append(int(input("Enter Element")))
print(lst)

se = int(input("Enter the Element to be search"))
for i in range(len(lst)):
    if lst[i] == se:
        p = i
        print(se, "Found at Position ", p)
        break
else:
    print("Element Not Found")

