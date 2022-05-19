n=int(input())
count=0
count1=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
for i in range (1,rev+1):
    if rev%i==0:
        count1=count1+1
        
if count==2 and count1==2:
    print('circular prime')
elif count==2:
    print('prime but not a circular prime')
else:
    print('not prime')