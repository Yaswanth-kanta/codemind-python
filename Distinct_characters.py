s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
st='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'
for i in a:
    if i==' ':
        continue
    st+=i
print(st)