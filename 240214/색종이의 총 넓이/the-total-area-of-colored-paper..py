N = int(input())
arr = [[0]*201 for _ in range(201)]
for _ in range(N):
    x1,y1= map(int,input().split())
    x1+=100
    y1 += 100
    x2 = x1+8
    y2 = y1+8
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] +=1
cnt = 0
for i in range(201):
    for j in range(201):
        if arr[i][j]>=1 :
            cnt += 1
print(cnt)