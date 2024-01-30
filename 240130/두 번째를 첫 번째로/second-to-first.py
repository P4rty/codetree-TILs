s = input()
arr = list(s)
ch = arr[0]
ql = arr[1]

for i in range(len(arr)):
    if arr[i] == ql:
        arr[i] = ch
s = ''.join(arr)
print(s)