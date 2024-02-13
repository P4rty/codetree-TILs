n = int(input())
arr = [0]*2001
idx = 1000
for i in range(n):
    x,direction = input().split()
    x = int(x)+1000
    if direction == "L":
        for j in range(idx,x+1):
            arr[j] +=1
        idx = x+1
    elif direction == "R":
        for j in range(x,idx+1):
            arr[j] +=1
        idx = x

ck = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        arr[i] = 1
    else:
        arr[i] = 0
mk = 0
for i in range(len(arr)):
    if arr[i] == 1:
        ck += 1
    if arr [i] != arr[i-1]:
        ck -= 1
print(ck)