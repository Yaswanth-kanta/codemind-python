_=int(input())
v=list(map(int,input().split()))
a=b=0
for k in range(0,len(v)-2,2):
    b+=1
    if(v[k+1]>v[k] and v[k+1]>v[k+2]):
        a+=1
if(a==b):
    print(a)
else:
    print(-1)