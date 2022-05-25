n=int(input())
b=list(map(int,input().strip().split()))[:n]
c=b[::-1]
for i in range(n//2):
    print(c[i],end=' ')
for i in range(n//2):
    print(b[i],end=' ')