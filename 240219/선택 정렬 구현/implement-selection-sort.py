n = int(input())
arr = list(input().split())
for i in range(len(arr)-1):
    min_idx = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    tmp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = tmp
for i in range(len(arr)):
    print(arr[i],end=" ")