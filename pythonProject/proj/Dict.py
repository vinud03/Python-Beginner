#Dictionary is nothing but key value pairs

d1={}
d2={'Gana':'veg','kunal':'Chicken','Nitin':'Paneer',
    'Nishant':{'B':'maggie','lunch':'Rosita','Dinner':'Michone'}}
d2['Akshay']='Chinese'
print(d2["Nishant"]['B'])
print(d2
      )
del d2['Akshay']
print(d2)

d3=d2.copy()
print(d3)
del d3['Nishant']
d2.get('Gana')
d2.update({'Gana':'Tikka'})
print(d3.items())
print(d2.keys())
print(d2.values())

