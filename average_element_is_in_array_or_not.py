n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
for i in a:
    if i==avg:
        print("True")
        break
else:
    print("False")

