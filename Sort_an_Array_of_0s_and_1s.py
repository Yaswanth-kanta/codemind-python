a=int(input())
b=list(map(int,input().split()))[:a]
b.sort()
for i in b:
    print(i,end=" ")