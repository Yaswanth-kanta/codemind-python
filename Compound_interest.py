import math
p,r,t=map(int,input().split())
d=math.pow(1+r/100,t)
print('{:.2f}'.format(p*d))