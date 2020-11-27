def Person(name, *data):
    print(name)
    for i in data:
        print(i)
Person('bibin', 28, 'Kuttampuzha', 7356951291)