def radix_sort(arr, k):
    for pos in range(k - 1, -1, -1):
        arr_new = [[] for _ in range(10)]
        for i in range(len(arr)):
            digit = (arr[i] // (10 ** pos)) % 10
            arr_new[digit].append(arr[i])

        store_arr = []
        for i in range(10):
            store_arr.extend(arr_new[i])

        arr = store_arr

    return arr

n = int(input())
arr = list(map(int,input().split()))
k = len(str(max(arr)))
result = radix_sort(arr,k)
for num in result:
  print(num,end=" ")