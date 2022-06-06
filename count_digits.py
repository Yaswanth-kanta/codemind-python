n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    b.append(abs(i))
for i in b:
    print(len(str(i)),end=' ')