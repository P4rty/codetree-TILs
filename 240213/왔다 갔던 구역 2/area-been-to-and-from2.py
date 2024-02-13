n = int(input())
arr = [0]*2001
idx = 1000
for i in range(n):
    x,direction = input().split()
    x = int(x)+1000
    if direction == "L":
        arr[idx:x] = [val + 1 for val in arr[idx:x]]
        idx = x + 1
    elif direction == "R":
        arr[x:idx] = [val + 1 for val in arr[x:idx]]
        idx = x

ck = sum(1 for val in arr if val >= 2)
print(ck-1)