n,k,T = input().split()
len_t = len(T)
n= int(n)
k = int(k)
arr = []
for _ in range(n):
    s = input()
    if T in s[0:len_t] :
        arr.append(s)
arr= sorted(arr)
print(arr[k-1])