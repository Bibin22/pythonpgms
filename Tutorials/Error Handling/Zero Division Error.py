a = 5
b = 0
try:
    print(a / b)
except Exception as e:
    print("number cant divided by zero", e)
finally:
    print("it will execute if there is a error occured or not")
