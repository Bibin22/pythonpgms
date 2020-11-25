bibin = {'name':'bibin', 'age':23, 'dob':'23/07/1997'}
print(bibin)
print(bibin.get('name'))
bibin['place'] = 'kuttampuzha'
bibin['number'] = 7356951291
print(bibin)
print(bibin['place'])

print("key and values are")
for key, value in bibin.items():
    print(key,':',value)

print("keys are")
for key in bibin.keys():
    print(key)

print("values are")
for val in bibin.values():
    print(val)