s=input()
s=s.split(' ')
v=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    x=list(i)
    a=[]
    for j in x:
        if j not in v:
            a.append(j)
    a.sort()
    y=0
    for k in range(len(x)):
        if x[k] not in v:
            print(a[y],end='')
            y+=1
        else:
            print(x[k],end='')
    print(end=' ')
