print('1.capitalize(): Converts the first character to upper case')
txt1 = 'hello world'
print('input =', txt1)
print('output =', txt1.capitalize())

print('2.casefold():Converts string into lower case')
txt2 = 'HELLO WORLD'
print('input =', txt2)
print('output = ', txt2.casefold())

print('3.center(): 	Returns a centered string')
txt3 = 'Hello World'
print('input =', txt3)
print('output =', txt3.center(50))

print('4.count(): Returns the number of times a specified value occurs in a string')
txt4 = 'I love apples, apple are my favorite fruit'
print('input = ', txt4)
print('output =', txt4.count('apple'))

print('5.encode(): Returns an encoded version of the string')
txt5 = 'My name is Ståle'
print('input =', txt5)
print('output =', txt5.encode())

print('6.endswith(): Returns true if the string ends with the specified value')
txt6 = 'hello world.'
print('input =', txt6)
print('output', txt6.endswith('.'))

print('7.expandtabs(): Sets the tab size of the string')
txt7 = 'H\te\tl\tl\to'
print('input =', txt7)
print('output =',txt7.expandtabs(1))

print('8.find(): Searches the string for a specified value and returns the position of where it was found')
txt8 = 'hello world'
print('input =', txt8)
print('output =', txt8.find('world'))

print('9.format(): Formats specified values in a string')
txt9 ='For only {price:.2f} dollars!'
print('input=', txt9)
print('output=',txt9.format(price = 49))
print('format() examples')
ftxt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
ftxt2 = "My name is {0}, I'am {1}".format("John",36)
ftxt3 = "My name is {}, I'am {}".format("John",36)
print(ftxt1)
print(ftxt2)
print(ftxt3)

print('10.index():Searches the string for a specified value and returns the position of where it was found')
txt10 ='hello world'
print('input =', txt10)
print('output =', txt10.index('world'))
print('index(): exaple')
print('output of example =', txt10.index('l', 4, 10))

print('difference between find() and index()')
print('If the value is not found, the find() method returns -1, but the index() method will raise an exception(error)')

dtxt = "Hello, welcome to my world."

print(dtxt.find("q"))
#print(dtxt.index("q"))

print('11.join():Joins the elements of an iterable to the end of the string')
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

print('12.ljust():Returns a left justified version of the string')
txt11 = 'hello'
print(txt11.ljust(20),'world')
print(txt11.ljust(20,'-'),'world')

print('13.maketrans().Returns a translation table to be used in translations')
txt12 = 'Sam'
print('input=', txt12)
mytable = txt12.maketrans("S", "P");
print('output=',txt12.translate(mytable));

print('maketrans()example')

mtxt = "Hi Sam!";
print('input=', mtxt)
x = "Sam";
y = "Joe";

mytable = mtxt.maketrans(x, y);

print('output =',mtxt.translate(mytable));
print('13.partition(): Returns a tuple where the string is parted into three parts')
txt13 = "I could eat bananas all day"
print('input =', txt13)
print('output =', txt13.partition("bananas"))

print('14.rfind():Searches the string for a specified value and returns the last position of where it was found')
txt14 = "Hello, welcome to my world."
print('input=', txt14)
print('output=',txt14.rfind("e"))# this 'e' found from the word 'welcom e'

print('15.rindex():Searches the string for a specified value and returns the last position of where it was found')
txt15 = "Mi casa, su casa."
print('input =', txt15)
print('output=', txt15.rindex("casa"))

print('16.rjust():Returns a right justified version of the string')
txt16 = 'hello'
print('input=', txt16)
print(txt16.rjust(20),)

print('17.splitlines():Splits the string at line breaks and returns a list')
txt17 = "Thank you for the music\nWelcome to the jungle"
print('input =', txt17)
print('output=', txt17.splitlines())

print('18.startswith():Returns true if the string starts with the specified value')
txt18 = 'hello world'
print(txt18.startswith('h'))

print('19.strip():Returns a trimmed version of the string')
txt19 ='     banana    '
print('input =', txt19)
print('output=', txt19.strip())

print('20.swapcase():Swaps cases, lower case becomes upper case and vice versa')
txt20 = 'HeLlO WOrLd BibIN'
print('input =', txt20)
print('output =', txt20.swapcase())

print('21.title():Converts the first character of each word to upper case')
txt21 = 'hello world bibin'
print('input =', txt21)
print('output=', txt21.title())

print('22.translate():Returns a translated string')
mydict = {83:  80};
ttxt = "Hello Sam!";
print(ttxt.translate(mydict));


print('23.zfill():Fills the string with a specified number of 0 values at the beginning')
txt22 = '7'
print('input=', txt22)
print('output =', txt22.zfill(3))