import pyttsx3

l1=['Bhendi','Gajar','Kobi','Ratali','batata','Mula','Kanda']

print(l1[::2])
i=1
s=pyttsx3.init()
print('\n \n ')
for item in l1:
    if i%2!=0:
        print(f"Jarvis buy {item}")
    i+=1
print('\n \n')
for index,items in enumerate(l1):
    if index%2==0:
        k=f"Jarvis {items} lana"
        s.say(k)
        s.runAndWait()

#
#
# l1=('Gana','Sayali','Jamurt','Kavita')
# for index,item in enumerate(l1):
#     if index%2==0:
#         print(item)