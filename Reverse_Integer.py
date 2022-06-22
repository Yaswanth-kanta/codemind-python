n=int(input())
res=str(n)
if n<0:
    res='-'+res[::-1][:-1]
    n=int(res)
    print(n)
else:
    res=res[::-1]
    n=int(res)
    print(n)