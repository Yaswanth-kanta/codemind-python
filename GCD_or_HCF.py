def hcf(x,y):
    if x>y:
        c=y
    else:
        c=x
    for i in range(1,c+1):
        if(x%i==0) and (y%i==0):
            hcf=i 
    return hcf
a,b=map(int,input().split())
print(hcf(a,b))
