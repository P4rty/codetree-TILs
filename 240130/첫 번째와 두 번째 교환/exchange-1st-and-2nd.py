a = input()
arr = list(a)
check = arr[0]
change = arr[1]
for i in range(len(arr)):
    if arr[i] == check:
        arr[i] = change
    elif arr[i] == change:
        arr[i] = check
a = ''.join(arr)
print(a)