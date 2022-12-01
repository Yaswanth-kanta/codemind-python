s=input()
t='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'
z=''
for i in s:
    if i.isalpha():
        t+=i
j=len(t)-1
s=list(s)
for i in range(len(s)):
    if s[i].isalpha():
        s[i]=t[j]
        j-=1
for i in s:
    print(i,end='')