def digit(s):
    for i in s:
        if i.isdigit():
            return True
    return False

s=int(input())
while(s):
    a=input()
    if digit(a):
        print('Yes')
    else:
        print('No')
    s=s-1
