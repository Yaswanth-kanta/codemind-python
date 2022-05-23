def add(t):
    su=0
    for i in t:
        if i.isdigit()==True:
            su=su+int(i)
    return su
n=input()
print(add(n))

