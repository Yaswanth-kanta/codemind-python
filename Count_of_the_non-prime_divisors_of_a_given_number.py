def pri(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
t=int(input())
c=0
for i in range(1,t+1):
    if t%i==0:
        if not pri(i):
            c+=1
print(c)