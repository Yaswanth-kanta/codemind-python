def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n1=int(input())
n2=int(input())
res=n1+n2
for i in range(res+1,1000):
    if prime(i):
        res1=i
        break
print(res1-res)