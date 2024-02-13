n = int(input())
arr = [0]*201
for i in range(n):
    x1,x2 = map(int,input().split())
    x1 += 100
    x2 += 100
    for j in range(x1,x2+1):
        arr[j] += 1
print( max(arr))