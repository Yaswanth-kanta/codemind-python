s=input()
s=s.split()
for i in s:
    x=list(i)
    a=[]
    for j in x:
        if j.isalpha():
            a.append(j)
    a.sort()
    y=0
    for k in range(len(x)):
        if x[k] not in a:
            print(x[k],end='')
        else:
            print(a[y],end='')
            y+=1
    print(end=' ')