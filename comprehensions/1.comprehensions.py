L1 = [x**3 for x in range(10)]
print(L1)
L2 = [3**x for x in range(2, 10, 1)]
print(L2)
L3 = [x for x in L2 if x%5==0]
print(L3)
String = "Winter is comming".split()
print(String)
String_cases=[[w.upper(), w.lower(), len(w)] for w in String]
print(String_cases)
for i in String_cases:
    print(i)
list1 = [1, '4', 9, 'a', 0, 4]
square_int = [ x**2 for x in list1 if type(x)==int]
print(square_int)