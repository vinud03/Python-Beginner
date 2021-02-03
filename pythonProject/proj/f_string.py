me='gana'
add='ghatkopar'

# using %s operator
k='This is %s from %s'%(me,add)
print(k)

# using .format()
j='This is {} from {}'.format(me,add)
print(j)

# using fstring
a=f'This is {me} from {add}'
print(a)