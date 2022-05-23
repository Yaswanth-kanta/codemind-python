n=input()
v=0
c=0
d=0
s=0
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        v=v+1
    elif i>='0' and i<='9':
        d=d+1
    elif i==' ':
        s=s+1
    else:
        c=c+1
print('Vowels: {}'.format(v))
print('Consonants: {}'.format(c))
print('Digits: {}'.format(d))
print('White spaces: {}'.format(s))
    