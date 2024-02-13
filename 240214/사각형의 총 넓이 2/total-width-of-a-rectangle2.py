N = int(input())
arr = [[0]*200 for _ in range(200)]
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] += 1
cnt = 0
for i in range(200):
    for j in range(200):
        if arr[i][j]>=1:
            cnt += 1
print(cnt)