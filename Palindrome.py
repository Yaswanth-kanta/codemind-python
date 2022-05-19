n=int(input())
rev=0
temp=n
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==temp:
    print('True')
else:
    print('False')