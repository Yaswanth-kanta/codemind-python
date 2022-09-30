n=int(input())
a=list(map(int,input().split()))
a.append(a[0])
a.append(a[1])
c=0
for i in range(1,len(a)-1):
    if (a[i-1]%2==0 and a[i+1]%2) or (a[i-1]%2 and a[i+1]%2==0):
        c+=1
print(c)