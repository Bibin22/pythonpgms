#f = open("bibin.py", "w")
#f.write("print('hello world')")
#f.close()
with open("bibin.py","r") as f:
    x = f.read()
print(x)