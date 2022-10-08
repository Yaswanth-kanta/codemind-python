s=input()
t="aeiou"
c=0
d=0
for i in s:
    if i in t:
        c+=1
        if c>d:
            d=c
    else:
        c=0
print(max(c,d))
    
           