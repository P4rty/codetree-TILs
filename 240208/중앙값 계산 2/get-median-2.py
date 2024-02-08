n = int(input())
arr = list(map(int,input().split()))
arr_2 = []
for i in range(n):
    arr_2.append(arr[i])
    if i % 2 == 0:
        arr_2 = sorted(arr_2)
        print(arr_2[(len(arr_2)//2)],end=" ")