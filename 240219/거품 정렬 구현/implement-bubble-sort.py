n = int(input())
arr = list(map(int,input().split()))
k = len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp

for i in range(n):
    print(arr[i],end = " ")