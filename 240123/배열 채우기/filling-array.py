li = list(map(int,input().split()))
arr = []
for element in li:
    if element==0:
        break
    arr.append(element)
for i in range(len(arr)-1,-1,-1):
    print(li[i],end=" ")