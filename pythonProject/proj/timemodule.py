import time

initial = time.time()
k=0
while(k<45):
   print("This is just try")
   k=k+1
print("While loop ran in",time.time()-initial,"Seconds")

for i in range(45):
    print("This is just try")
print("For loop ran in",time.time()-initial,"Seconds")


localtime=time.asctime(time.localtime(time.time()))
l=time.asctime()
print(l)
print(localtime)