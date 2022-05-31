a=list(map(int,input().split()))[:3]
b=list(map(int,input().split()))[:3]
al=0
bl=0
for i in range(0,3):
    if a[i]>b[i]:
        al+=1
    elif a[i]<b[i]:
        bl+=1
print(al,bl)
