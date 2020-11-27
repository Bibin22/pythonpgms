

a = [1, 2, 3, 4, 5, 6, 7, 8]
s = 2
i = 0
p = 0
while i <= len(a):
    if a[i] == s:
        p = i
        print(s,'found at ', p+1)
        break
    i = i + 1
else:
    print("Not found")



