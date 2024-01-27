arr2d=list()
for i in range(4):
    arr = list(map(int,input().split()))
    arr2d.append(arr)
sk=0
for j in range(4):
    for k in range(j+1):
        sk += arr2d[j][k]
print(sk)