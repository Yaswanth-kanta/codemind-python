n,d=map(int,input().split())
n=str(n)
x=(n[0:d])
y=(n[::-1])
z=(y[0:d])
z=z[::-1]
print(abs(int(x)-int(z)))