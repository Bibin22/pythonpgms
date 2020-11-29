def conlist(list):
	res= ''
	for i in list:
		res += str(i)
	return res
		
list = [1, 2, 3, 4, 5, 6]		
reslt = conlist(list)
print(reslt)