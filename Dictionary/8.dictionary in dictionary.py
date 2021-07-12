details = {
    'bibin':{'name':'Bibin Joy',
             'age':23,
             'dob':'23/07/1997',
             'place':'Kothamnagalam'},
    'nnn':{
        'name':'bibinn',
        'age':22,
        'dob':'12/03/1997',
        'place':'kk',
    }
}
print(details)
for name, detail in details.items():
    print(name,':')
    for key, val in detail.items():  
        print(key, val)
