n=int(input())
b=[]
for i in range(n+1):
    a=int(input())
    b.append(a)
t=b[n]
c=0
for i in range(n):
    if b[i]<=t:
        c+=1
    else:
        c+=2
print(c)
        
    