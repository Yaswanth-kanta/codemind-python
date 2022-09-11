for i in range(int(input())):
    n=int(input())
    n=str(n)
    a=[]
    for i in range(len(n)):
        a.append(int(n[i]))
    for i in range(min(a),max(a)+1):
        if i not in a:
            print('NO')
            break
    else:
        print('YES')