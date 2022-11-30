s1=input().lower()
s2=input().lower()
a=[]
for i in s1:
    if i in s2:
        if i not in a and i!=' ':
            a.append(i)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if ord(a[i])>ord(a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
if a==[]:
    print(-1)
else:
    for i in a:
        print(i,end='')