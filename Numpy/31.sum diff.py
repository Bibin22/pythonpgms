def sumdiff(a, b):
	sum = a + b
	diff = a - b
	if a == b or sum == 5 or diff == 5:
		return True
	else:
		return False
a = int(input("Enter a 1st Number"))
b = int(input("Enter 2nd Number"))
res = sumdiff(a, b)
print(res)