n = int(input())
color = 1 # 빨간색
arr = [[0]*201 for _ in range(201)]
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = color
    
    if color == 1:
        color = 2
    else: 
        color = 1

cnt = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 2:
            cnt += 1
print(cnt)