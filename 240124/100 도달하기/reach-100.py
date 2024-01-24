n= int (input())
arr=[]
arr.append(1)
arr.append(n)
print(arr[0],end=" ")
print(arr[1],end=" ")
for i in range(2,50):
    arr.append(arr[i-1]+arr[i-2])
    print(arr[i],end=" ")
    if arr[i]>100:
        break