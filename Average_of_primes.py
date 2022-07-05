def pri(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if pri(i):
        s.append(i)
print("{:.2f}".format(sum(s)/len(s)))
