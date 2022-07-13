n=int(input())
a=list(map(int,input().split()))
s=""
for i in a:
    s=s+str(i)
print(int(s,2))