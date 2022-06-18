n=int(input())
a=list(map(int,input().split()))
su=0
for i in a:
    if not i%2:
        su+=i
print(su)