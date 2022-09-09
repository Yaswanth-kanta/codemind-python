n=int(input())
a=list(map(int,input().split()))
p=int(input())
for i in range(p):
    x=a.pop()
    a.insert(0,x)
print(*a)