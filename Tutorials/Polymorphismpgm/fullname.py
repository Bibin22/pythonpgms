class Name:

    def __init__(self, name):
        self.name = name

    def __add__(first, second):
        name = first.name + second.name

        return name


first = Name("bibin")
second = Name("joy")
full = first + second
print(full)
