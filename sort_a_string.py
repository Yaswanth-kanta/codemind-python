s=input()
a=[]
for i in s:
    if i.isalpha():
        a.append(i)
k=0
a.sort()
for i in s:
    if i.isalpha():
        i=a[k]
        k+=1
    print(i,end='')