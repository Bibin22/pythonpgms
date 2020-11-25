print('1.clear():Removes all the elements from the dictionary')
car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
print(car)

print('2.copy():Returns a copy of the dictionary')
car ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car2 = car.copy()
print((car2))

print('3.fromkeys():Returns a dictionary with the specified keys and value')
x = ('key1', 'key2', 'key3')
y = 0
print(dict.fromkeys(x, y))

print('4.get():Returns the value of the specified key')
print(car.get('year'))
print(car.get("price", 15000))

print('5.items():Returns a list containing a tuple for each key value pair')
print(car.items())
car['year']=2018
print(car.items())
print(car)#year changed from 1964 to 2018

print('6.keys():Returns a list containing the dictionary\'s keys')
print(car.keys())
car['color'] = 'white' # new key added
print(car.keys())

print('7.values():Returns a list containing the dictionary\'s values')
print(car.values())

print('8.pop():Removes the element with the specified key')
car.pop('color') #color removed
print(car)

print('9.popitem():Removes the last inserted key-value pair')
car.popitem() #year removed
print(car)

print('10.setdefault():Returns the value of the specified key. If the key does not exist: insert the key, with the specified value')
x = car.setdefault("model", "Bronco")
print(x)
car.setdefault("color", "black")
print(car)

print('11.update():Updates the dictionary with the specified key-value pairs')
car.update({'owner':'bibin'})
print(car)