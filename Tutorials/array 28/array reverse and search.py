from array import *
ar1 = array('i', [])
limit = int(input("Enter A Limit"))
for i in range(limit):
    ar1.append(int(input("Enter Array Elements:")))
print(ar1)
k = 0
se = int(input("Enter the value to be search"))
for j in ar1:
    if se == j:
        print(se, " found at  ", k, "Position")
        break
    k = k + 1
else:
    print("value not found")

ar2 = array(ar1.typecode, (a + a for a in ar1))
print("Sum of ar1", ar2)
ar3 = array(ar1.typecode, (a*a for a in ar1 ))
print("Mul of ar1", ar3)
print("Reverse of ar1")
for rev in range(len(ar1)-1, -1, -1 ):
    print(ar1[rev])

