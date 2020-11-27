from array import *
arr = array('i', [])
l = int(input("Enter the Limit"))
for i in range(l):
    arr.append(int(input("Enter array elements")))
print(arr)
n = int(input("Enter the Number to  be Search"))
l = 0
u = len(arr)-1
while l <= u:
    mid = (l + u) // 2
    if arr[mid] == n:
        p = mid
        print(n, "found at position", p)
        break
    elif arr[mid] < n :
        l = mid + 1
    elif arr[mid] > n :
        u = mid - 1
else:
    print("item not found")