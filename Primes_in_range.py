def pri(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
s=0
for k in range(a,b+1):
    if pri(k):
        s+=1
print(s)