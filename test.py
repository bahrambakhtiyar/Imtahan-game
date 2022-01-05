from random import *
n = int(input())
a=[]
i=0
while len(a)!=n:
    b=randint(1,1000)
    a.append(b)
say=0
for i in a:
    if i==1:
        say+=1
print(say)