def change_list(arr,n):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2

N = int(input())
brr = list(map(int,input().split()))
change_list(brr,N)

for elem in brr:
    print(elem,end = " ")