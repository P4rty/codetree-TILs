def f(arr,n):
    if n == 1:
        return arr[0]
    else:
        max_elem = f(arr,n-1)
        return max(max_elem, arr[n-1]) 


n = int(input())
arr= list(map(int,input().split()))
print(f(arr,n))