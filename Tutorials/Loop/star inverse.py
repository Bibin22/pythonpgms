from collections import namedtuple
a = namedtuple('Name', 'course, technology')
s = a('data science', 'python')
print(s)