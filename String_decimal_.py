n=int(input())
for i in range(n):
    c=0
    a=input()
    for i in a:
        if i.isdigit():
            c=c+1
    if c==len(a):
        print('True')
    else:
        print('False')
    
    
    