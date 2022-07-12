n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i%2 and i not in b:
        b.append(i)
print(len(b))