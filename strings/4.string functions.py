#UPPER AND LOWER FUNCTIONS

name = 'Bibin Joy  '
print(name.upper())#full cap letter
print(name.lower())#full small letter
print("**************END OF UPPER and LOWER functions ***************")



#lstrip and rstrip
language = ' python '
print(language)
print(language.rstrip())#remove right whitespace
print(language.lstrip())#remove left whitespace

print("**************END OF rstrip  and lstrip functions ***************")
#find()

print(name.find('n'))#find the posion of 'n' in name

print("**************END OF Find functions ***************")


#replace()
print(language.replace('python', 'java'))# replace python to java
newlanguage = language.replace(' python ', 'java')
print(newlanguage)
print(name.replace('Bibin Joy', 'BibinJoy'))

print("**************END OF Replace functions ***************")
