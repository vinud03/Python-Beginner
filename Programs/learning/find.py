books=['sayali','kavita','jamrut','gana','kau']
print('enter the name of the book:')
check=input()
for book in books:
	if book == check:
		print('Yes, I do have that book')
		break
else:
		print('I do not have that book')
