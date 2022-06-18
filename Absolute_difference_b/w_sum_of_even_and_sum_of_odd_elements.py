n=int(input())
a=list(map(int,input().split()))
su=0
su1=0
for i in a:
    if i%2==0:
        su+=i
    else:
        su1+=i
print(abs(su-su1))
      