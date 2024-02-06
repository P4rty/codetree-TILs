def abs_list(arr,N):
    for i in range(N):
        arr[i]= abs(arr[i])
    return arr

N = int(input())
arr = list(map(int,input().split()))
arr = abs_list(arr,N)
for i in range(N):
    print(arr[i],end= " ")