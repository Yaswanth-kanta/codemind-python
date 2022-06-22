n=int(input())
d=[]
e=[]
a=0
b=1
for i in range(n):
    d.append(a)
    c=a+b
    a=b   
    b=c 
for i in range(n):
    if n>d[i] and n<d[i+1]:
       e.append(d[i])
       e.append(d[i+1])
if(n-e[0]>e[1]-n):
    print(e[1])
elif(n-e[0]<e[1]-n):
    print(e[0])
else:
    print(e[0],e[1])