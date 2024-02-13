N,K = map(int,input().split())
arr = [0]*(N+1)
for i in range(K):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        arr[j] += 1
print(max(arr))