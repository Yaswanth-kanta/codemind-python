n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
for i in a:
    if i>=x and i<=y:
        continue
    else:
        s+=i
print(s)
    