a,b=map(int,input().split())
arr= []
arr.append( a)
arr.append(b)
print(arr[0],end=" ")
print(arr[1],end=" ")
for i in range(2,10):
    arr.append((arr[i-1]+arr[i-2])%10)
    print(arr[i],end=" ")