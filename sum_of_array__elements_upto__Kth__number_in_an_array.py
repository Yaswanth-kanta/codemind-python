n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in a:
    if i!=b:
        s+=i
    else:
        s+=i
        break
print(s)