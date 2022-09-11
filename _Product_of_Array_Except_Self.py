n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    r=1
    for j in range(n):
        r=r*a[j]
    print(r//a[i],end=' ')
        
    