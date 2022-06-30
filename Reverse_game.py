n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    r=str(i)[::-1]
    b.append(int(r))
print(*b)