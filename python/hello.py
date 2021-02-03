n = int(input())
m=bin(n).replace("0b","")
m=str(m)
print(m)
ls=[]
cnt=1
for i in range(len(m)-1):
    if m[i]==m[i+1]:
        cnt+=1
    else:
        ls.append(cnt)
        cnt=1
ls.append(cnt)
print(ls)
type()
# print(max(ls))
datatype()