n=int(input())
count=0
for i in range (n):
    if n==i*(i+1):
        count=1
        break
if count==1:
    print('YES')
else:
    print('NO')
    