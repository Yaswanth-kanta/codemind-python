line=input()
inp=line.split(":")
h=inp[0]
m=inp[1]
a=abs((int(h)*30)-(11*int(m))/2)
if(a<360-a):
    if(a>(int(a))):
        print(a)
    else:
        print(float(a))
else:
    if(360-a>int(360-a)):
        print(360-a)
    else:
        print(float(360-a))
   