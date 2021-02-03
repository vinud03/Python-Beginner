# f=open('gana1.txt','w')  #always open file in write mode to do write operation otherwise programs gives us error
# f.write("Vinayak is Smart boy")  # write function clear the file and then write the given content
#
# f.close()



# f=open('gana.txt','a')  #always open file in write mode to do write operation otherwise programs gives us error
# a=f.write("Vinayak is Smart boy\n")  # write function clear the file and then write the given content
# print(a)
# f.close()


# Read and write

# f=open('gana.txt','r+')
# content=f.read()
# print(content)
# f.write('Thank you\n')
# print(content)

# f.close()


# seek() tell() function
'''f=open('gana.txt')
print(f.tell())
print(f.readlines())
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline())
print(f.tell())
f.close()'''

with open('gana.txt') as f:
    a=f.read(5)
    print(a)

f=open('gana.txt','rt')
print(f.readline())
f.close()