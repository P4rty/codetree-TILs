n = int(input())
arr = [0]*2001
idx = 1000
for i in range(n):
    x,direction = input().split()
    x = int(x)
    if direction == "L":
        for j in range(idx-x,idx):
            arr[j] += 1
            idx -=1
    elif direction == "R":
        for j in range(idx,idx+x):
            arr[j] += 1
            idx +=1

ck = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        ck += 1
    
print(ck)