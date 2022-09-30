n=int(input())
a=list(map(int,input().split()))
o=[]
e=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in range(min(len(e),len(o))):
    print(o[i],end=' ')
    print(e[i],end=' ')
if len(e)>len(o):
    for i in range(len(o),len(e)):
        print(e[i],end=' ')
if len(e)<len(o):
    for i in range(len(e),len(o)):
        print(o[i],end=' ')
if n%2:
    print(0)