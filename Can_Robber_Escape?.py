n=int(input())
count=0
a=list(map(int,input().split()))
for i in a:
    if i%2!=0:
        count=count+1
if count<=2:
    print('YES')
else:
    print('NO')