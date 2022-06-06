def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=[]
for i in range(2,n):
    if n%i==0:
        if prime(i):
            a.append(i)
b=[]
for i in a:
    for j in a:
        if n==i*j:
            if i not in b and j not in b:
                b.append(i)
                b.append(j)
if b==[]:
    print(-1)
else:
    print(*b)
       
       
   
       
            
        