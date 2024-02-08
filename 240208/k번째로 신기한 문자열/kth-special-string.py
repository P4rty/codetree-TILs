n,k,T = input().split()
n= int(n)
k = int(k)
arr = []
for _ in range(n):
    s = input()
    if T in s:
        arr.append(s)
arr= sorted(arr)
print(arr[k-1])