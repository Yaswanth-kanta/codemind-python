s=input()
s=s.lower()
s=s.split()
x=s[0]
y=s[1]
a=[]
b=[]
for i in x:
    if i in y:
        a.append(i)
for i in a:
    c=0
    for j in s:
        if i in j:
            c+=1
    if c==len(s):
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(min(b))