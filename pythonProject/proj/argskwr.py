def funargs(normal,*args,**kwargs):               # Here normal is normal argument and *args is multiple argument input it get the input in tupple form
    print(normal)
    for i in args:
        print(i)
    print('\n')
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


normal = 'I am normal'
name =['gana', 'sayali', 'kunal', 'harry']
kw={'Gana':'Monitor', "Sayali":'Fitness Instructor', 'Kunal':'Youtuber', "Harry":'Programmer'}


funargs(normal,*name,**kw)   #we are giving normal argument and multiplt argument using *name.
