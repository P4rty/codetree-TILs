li = list(map(int,input().split()))
arr = []

for element in li:
    if element==0:
        break
    arr.append(element)
sum = 0
cnt = 0
for i in range(len(arr)-1,-1,-1):
    if arr[i] %2 ==0:
        sum+=arr[i]
        cnt +=1
print(f'{cnt} {sum}')