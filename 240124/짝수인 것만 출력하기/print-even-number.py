n= int(input())
arr=map(int,input().split())
arr = list(arr)
new_arr=[]

for i in range(n):
    if arr[i] % 2 ==0:
        new_arr.append(arr[i])
        print(arr[i],end=" ")