def selection_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr-1):
        min = i
        for j in range(i+1,len_arr):
            if arr[j] < arr[min]:
                min = j
            tmp = arr[i]
            arr[i] = arr[min]
            arr[min] = tmp
    return arr

n = int(input())
arr = list(input().split())
selection_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")