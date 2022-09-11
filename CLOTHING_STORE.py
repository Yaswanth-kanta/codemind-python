n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
c=0
for i in b:
    if a.count(i)>2:
        c+=a.count(i)//2
    elif a.count(i)==2:
        c+=1
print(c)
    
