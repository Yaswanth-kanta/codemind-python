n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
a.sort()
if len(a)<3:
    print(max(a))
else:
    print(a[-3])
