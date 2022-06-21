def sel(n):
    c=0
    temp=n
    while n:
        r=n%10
        if r!=0:
            if temp%r==0:
                c+=1
        n=n//10
    if len(str(temp))==c:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if sel(i):
        print(i,end=' ')