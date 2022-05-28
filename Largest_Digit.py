n=int(input())
r=n%10
while(n):
    r1=n%10
    if r1>r:
        r=r1
    n=n//10
print(r)