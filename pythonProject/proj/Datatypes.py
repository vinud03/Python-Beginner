"""
#data types.
a=5
b=47.5
c=1+2j
print(type(a))
print(type(b))
print(type(c))
print("a is a Integer Number:",isinstance(a,int))
print("b is a float Number:",isinstance(b,float))
print("c is a Complex number:",isinstance(c,complex))
"""

#List
'''
S=[1,"hi","python",2]
print(type(S))
print(S)
print(S[3:])
print(S[0:2])
print(S+S)
print(S*3)
'''

# Creating Empty set
set1 = set()

set2 = {'James', 2, 3, 'Python'}

# Printing Set value
print(set2)

# Adding element to the set

set2.add(10)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)