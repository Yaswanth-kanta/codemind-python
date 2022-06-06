n,m=map(int,input().split())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:m]
c=set(a)
d=set(b)
e=c.intersection(d)
f=c.union(d)
g=list(e)
h=list(f)
for i in g:
    if i in h:
        h.remove(i)
print(len(h))
        