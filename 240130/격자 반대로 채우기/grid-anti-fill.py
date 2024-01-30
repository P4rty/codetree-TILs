n = int(input())
arr = [[0]* n   for _ in range(n)]
num =0
direction = -1
for i in range(n-1,-1,-1):  
    direction *= -1
    if direction == 1:
        for j in range(n-1,-1,-1):
            num+=1
            arr[j][i] = num
        continue
    if direction == -1:
        for j in range(n):
            num+=1
            arr[j][i] = num
        continue
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()