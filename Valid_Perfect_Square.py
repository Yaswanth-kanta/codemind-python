def valsqr(n):
    for i in range(1,n+1):
        if n==i*i:
            return True
   
t=int(input())
while(t):
    a=int(input())
    if valsqr(a):
        print("True")
    else:
        print('False')
    t=t-1