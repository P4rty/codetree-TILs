arr1 = list(map(int, input().split()))
arr = []

for element in arr1:
    if element == 0:
        break
    arr.append(element)

a = sum(arr[-3:])
print(a)