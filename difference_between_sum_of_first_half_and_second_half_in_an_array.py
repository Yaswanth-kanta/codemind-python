n=int(input())
a=list(map(int,input().split()))
m=len(a)//2
s=0
s1=0
for i in range(m):
    s+=a[i]
for i in range(m,len(a)):
    s1+=a[i]
print(abs(s-s1))