import datetime
print(datetime.datetime.now())
print(datetime.date.today())
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))
print(datetime.date.today().month)
x = datetime.datetime(2020,9,30)
print(x)
y = datetime.datetime(2019,9,30)
dif = x - y
print(dif)
end = datetime.datetime.now()
differrence = end - now
print(differrence)