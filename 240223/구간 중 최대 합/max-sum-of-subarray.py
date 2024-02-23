n,k = map(int,input().split())
arr = list(map(int,input().split()))
max_val = 0
for i in range(0,n-k+1):
    sum_some = 0
    for j in range(i,i+k):
        sum_some += arr[j]
    max_val = max(max_val,sum_some)
print(max_val)