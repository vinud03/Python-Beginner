# File IO basics
'''
"r" - open file for reading         #defualt mode
"w" - open file for writing
"x" - creates file if not exist
"a" - add more content to a file
"t" - text mode                     #default mode
"b" - binary mode
"+" - read and write

'''

f= open("gana.txt")
# content=f.read(3)   # Once u read a file, we can't read it again.
# print(content)
# content=f.read(3)
# print(content)

# print(f.readline())  # read line read single line only
# print(f.readline())  # read next unreadline line


print(f.readlines())  # store all unread lines in List.    if we read any lines before this that lines can't be there in list.  It read only unread lines.

f.close()