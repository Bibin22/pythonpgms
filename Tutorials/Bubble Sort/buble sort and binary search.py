from array import *
arr = array('i',[])
li = int(input("Enter the limit"))


for i in range(li):
    arr.append(int(input("Enter array Element")))
print(arr)

#Buble Sort
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j] > arr[j+1]:
             arr[j], arr[j + 1] = arr[j + 1], arr[j]
print('Sorted array', arr)


#Binary SEarch

se = int(input("Enter the number to be search"))
l = 0
u = len(arr)-1
while l <= u:
    mid = (l + u) // 2
    if arr[mid] == se:
        p = mid
        print(se, "found at ", p)
        break
    elif arr[mid] < se :
        l = mid + 1
    elif arr[mid]> se :
        u = mid -1
else:
    print("item not found")