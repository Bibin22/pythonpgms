name = 'spam'
print(name)
#name[0]  = 'z'# string is inmutable
#print(name)


#to alter string


name = 'z' + name[1:]
print(name)
name = name[0:] + 'ing'
print(name)