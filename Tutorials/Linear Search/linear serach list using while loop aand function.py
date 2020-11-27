def search(list, s):
    i = 0

    while i <= len(list):
        if list[i] == s:

            print(s,'found at ')
        i = i + 1
    else:
        print("not found")


list = []
for j in range(5):
    list.append(int(input("Enter list elments")))
print(list)
s = int(input("Enter a Number"))

search(list, s)
