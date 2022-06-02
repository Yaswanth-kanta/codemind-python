x,y=map(int,input().split())
a=list(map(int,input().split()))[:x]
b=list(map(int,input().split()))[:y]
c=set(a)
d=set(b)
e=c.intersection(d)
print(len(e))
