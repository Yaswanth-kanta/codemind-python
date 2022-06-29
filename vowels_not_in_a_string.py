a=['a','e','i','o','u']
b=[]
s=input()
for i in a:
    if s.count(i)==0:
        b.append(i)
if b==[]:
    print(0)
else:
    print(*b)

