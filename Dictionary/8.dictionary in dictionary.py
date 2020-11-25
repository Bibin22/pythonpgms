details = {
    'bibin':{'name':'Bibin Joy',
             'age':23,
             'dob':'23/07/1997',
             'place':'Kothamnagalam'},
    'ammu':{
        'name':'ammu',
        'age':22,
        'dob':'12/03/1998',
        'place':'Ettumanur',
    }
}
print(details)
for name, detail in details.items():
    print(name,':')
    for key, val in detail.items():  
        print(key, val)
