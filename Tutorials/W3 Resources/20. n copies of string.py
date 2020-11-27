def strings(str1, n):
    if len(str1) > 2:
        cp = n * (str1[0:2])
        return cp
    if len(str1) < 2:
        cpy = n * str1
        return cpy


str1 = input(" enter the string")
n = int(input(" number of copies"))
s = strings(str1, n)
print(s)
