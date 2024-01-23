n = int(input())
arr = list(map(int,input().split()))
arr1 = list()
for i in range(n-1,-1,-1):
    if arr[i] % 2 ==0:
        arr1.append(arr[i])

for i in range (len(arr1)):
    print(arr1[i],end=" ")