st=int(input())
a=list(map(int,input().split()))[:st]
et=int(input())
b=list(map(int,input().split()))[:et]
qt=int(input())
c=0
for i in range(0,st):
        if qt>=a[i] and qt<=b[i]:
            c=c+1
print(c)