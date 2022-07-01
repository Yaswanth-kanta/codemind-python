x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in b:
        if i in a:
            if i not in c:
                c.append(i)
print(len(c))

            