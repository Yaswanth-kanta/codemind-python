n=int(input())
a=list(map(int,input().split()))
for i in a:
    c=0
    b=[]
    for j in a:
        if i>j:
            c+=1
    b.append(c)
    print(*b,end=' ')