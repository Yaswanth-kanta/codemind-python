s=input()
s=s.split(' ')
s=s[-1]
s=list(s)
x=min(s)
if x.lower() in s:
    print(x.lower())
else:
    print(x)