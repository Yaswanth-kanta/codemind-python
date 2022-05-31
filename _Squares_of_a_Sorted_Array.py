n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    b.append(i*i)
b.sort()
print(*b)
    