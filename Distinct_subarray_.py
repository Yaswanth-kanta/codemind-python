a=int(input())
b=int(input())
arr=[]
v=0
c=0
for i in range(a,b+1):
    arr.append(i)
n=len(arr)
for i in range(n):
    v=0
    for j in range(i,n):
        v=v+arr[j]
        if v%2:
            c+=1
print(c)