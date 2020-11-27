from array import *
n = int(input("enter the limit"))
a = array("i", [])
for i in range(n):
    a.append(int(input("Enter array elements")))
print(a)

s = int(input("Enter The Value to be search"))
k = 0
for j in a:
    if j == s:
        print(s, "found at ", k, "th Position")
        #print(a.index(s)) inbuilt function to find index
        break
    k = k + 1
else:
    print("item not found")

print("Reverse of the Array")
for r in range(len(a)-1, -1, -1):

    print(a[r])