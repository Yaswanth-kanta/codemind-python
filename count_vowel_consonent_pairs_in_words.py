s=input()
s=s.split(' ')
v=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in s:
    x=i[0:len(i)//2]
    y=i[len(i)//2:len(i)]
    y=y[::-1]
    for j in range(min(len(x),len(y))):
        if(x[j] in v and y[j] not in v) or (x[j] not in v and y[j] in v):
            c+=1
print(c)