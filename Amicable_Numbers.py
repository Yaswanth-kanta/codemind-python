n1=int(input())
n2=int(input())
sum1=0
sum2=0
for i in range (1,n1):
    if n1%i==0:
        sum1=sum1+i
for j in range (1,n2):
    if n2%j==0:
        sum2=sum2+j
if n1==sum2 and n2==sum1:
    print('Amicable')
else:
    print('Not Amicable')
    