n=int(input())
a=list(map(int,input().split()))[:n]
print(max(set(a),key=a.count))

    