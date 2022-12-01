s=input()
t1=""
t2=""
t1=list(t1)
for i in range(0,s.index(' ')):
    t1+=s[i]
for i in range(s.index(' ')+1,len(s)):
    t2+=s[i]
t1=list(t1)
t2=list(t2)
for i in t1:
    if i not in t2:
        print('False')
        break
    else:
        t2.remove(i)
else:
    print('True')
