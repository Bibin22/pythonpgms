names ={
    'bibin':'python',
    'ammu':'python',
    'zack':'c',
    'paul':'cpp'

}

print(names)
print('sort key and values')
for key, val in sorted(names.items()):
    print(key,':',val)
print('sort key')
for keysort in sorted(names):
    print(keysort)

print('sort values')
for valsort in sorted(names.values()):
    print(valsort)
print('used values in names ')
for val in set(names.values()):
    print(val)