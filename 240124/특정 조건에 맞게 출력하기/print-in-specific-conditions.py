arr = list(input().split())

for i in range(len(arr)):
    arr [i] = int(arr[i])
    if arr[i] ==0:
        break
    elif arr[i] %2 ==1:
        arr[i]=arr[i]+3
    elif arr[i] % 2 ==0:
        arr[i]=arr[i]//2
    print(arr[i],end=" ")