n=int(input())
a=list(map(int,input().split()))
b=[]
l=n//2
for i in range(0,l):
    b.append(a[i])
    b.append(a[i+l])
print(*b)