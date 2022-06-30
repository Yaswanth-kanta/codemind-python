def su(n):
    s=0
    while(n):
        r=n%10
        s+=r
        n//=10
    return s
n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=su(i)
print(sum)