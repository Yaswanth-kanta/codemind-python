def fact(n):
    if n==0:
        return 0
    if n==1:
        return n
    else:
        return n*fact(n-1)
t=int(input())
while(t):
    a=int(input())
    if a>0:
        print(fact(a))
    t=t-1
        
    
    
