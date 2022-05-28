n=int(input())
a=[]
while(n):
    r=n%10
    a.append(r)
    n=n//10
for i in a:
    if a.count(i)!=1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')
    