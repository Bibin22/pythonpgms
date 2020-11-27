from array import *
vals = array('i', [1, 2, 3])
print("vals=", vals)
vals1 = array(vals.typecode, (a for a in vals))
print("copy of vals = ", vals1)

vals2 = array(vals.typecode, (a*a for a in vals))
print("Squre of vals =", vals2)

vals3 = array(vals.typecode, (a + a for a in vals))
print("sum of vals =", vals3)

vals4 = array(vals.typecode, (a - a for a in vals))
print("Sub of vals =", vals4)


