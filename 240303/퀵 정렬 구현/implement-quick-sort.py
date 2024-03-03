def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

n = int(input())
k = list(map(int,input().split()))
sorted_arr = quick_sort(k)
for i in range(n):
    print(sorted_arr[i],end = " ")