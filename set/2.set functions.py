print('1.add():Adds an element to the set')
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)

print('2.clear():Removes all the elements from the set')
car = {'maruti', 'benz', '800'}
car.clear()
print(car)

print('3.copy():Returns a copy of the set')
frt = fruits.copy()
print(frt)

print('4.difference():Returns a set containing the difference between two or more sets')
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}

print(x.difference(y))
print(y.difference(x))
z = {2, 3, 8, 9}
print(x.difference(y, z))

print('5.difference_update():Removes the items in this set that are also included in another, specified set')
p = {1, 2, 3}
q = {4, 5, 1}
print(p)
p.difference_update(q)
print(p)


print('6.discard():Remove the specified item')
birds = {'bat', 'parrot', 'peacock', 'crow'}
birds.discard('bat')
print(birds)



print('7.intersection():Returns a set, that is the intersection of two other sets')
a = {'x', 'y', 'z','q'}
b = {'z', 'x', 'p'}
print(a.intersection(b))
c = {'z', 's', 'q'}
print(a.intersection(b, c))


print('8.intersection_update():Removes the items in this set that are not present in other, specified set(s)')
a.intersection_update(b)
print(a)
a.intersection_update(b, c)
print(a)

print('9.isdisjoint():Returns whether two sets have a intersection or not')
a1= {"apple", "banana", "cherry"}
b1 = {"google", "microsoft", "facebook"}
print(a1.isdisjoint(b1)) # Return True if no items in set a1 is present in set b1:

a2 = {"apple", "banana", "cherry"}
b2 = {"google", "microsoft", "apple"}
print(a2.isdisjoint(b2))

print('10.issubset():Returns whether another set contains this set or not')

x1 = {'a', 'b', 'c'}
x2 = {'a', 'b', 'c', 'd'}
print(x1.issubset(x2))#Return True if all items set x1 are present in set x2:

print(x2.issubset(x1))#Return False if not all items in set x2 are present in set x1:

print('11.issuperset():Returns whether this set contains another set or not')
y1 = {'a', 'b', 'c'}
y2 = {'a', 'b'}
print(y1.issuperset(y2))#Return True if all items set y2 are present in set y1:
print(y2.issuperset(y1))#Return False if not all items in set y1 are present in set y2

print('12.pop():Removes an element from the set')
print(birds)
birds.pop()
print(birds)

print('13.remove()Removes the specified element')
print(fruits)
fruits.remove('cherry')
print(fruits)


print('14.symmetric_difference():Returns a set with the symmetric differences of two sets')
f1 = {"apple", "banana", "cherry"}
f2 = {"google", "microsoft", "apple"}
print(f1.symmetric_difference(f2))#Return a set that contains all items from both sets, except items that are present in both sets:

print('15.symmetric_difference_update():inserts the symmetric differences from this set and another')
print('f1=',f1)
print('f2=',f2)
f1.symmetric_difference_update(f2)#Remove the items that are present in both sets, AND insert the items that is not present in both sets:
print('f1=', f1)

print('16.union():Return a set containing the union of sets')
u1 = {'a', 'b', 'c'}
u2 = {'a', 'd', 'e'}
print(u1.union(u2))#Return a set that contains all items from both sets, duplicates are excluded:
u3 ={'e', 'f', 'g'}
print(u1.union(u2, u3))


print('17.update():Update the set with the union of this set and others')
up1 = {"apple", "banana", "cherry"}
up2 = {"google", "microsoft", "apple"}
up1.update(up2)#Insert the items from set up2 into set up1:
print(up1)