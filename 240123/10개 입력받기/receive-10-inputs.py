li = list(map(int,input().split()))
arr = []

for element in li:
    if element==0:
        break
    arr.append(element)
sum = 0
for i in range(len(arr)-1,-1,-1):
    sum += arr[i]
print('{0} {1:.1f}'.format(sum,sum/len(arr)))