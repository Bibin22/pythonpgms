a = 5
b =0
try:
    k = int(input("Enter a number"))
    print(k)
    print("Statement one")
    print(a/b)
    print("Statement two")

except ZeroDivisionError as e:
    print("Error Name is", e)
except ValueError as e:
    print("Error Name is", e)
except Exception as e:
    print("The Error I dont Know")
finally:
    print("finaly satament")
