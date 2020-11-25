hbbooks = {'programming in C#': 2014, 'Algorithms': 2015,'Python': 2016}
print(hbbooks.get('programming in C#'))
print(hbbooks.get('Algorithms'))
print(hbbooks.get('Python'))
print(hbbooks.get('Theory Theory, all the way', 'BadChoice'))