n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

cnt1 = 0
for i in range(n): # y ax
    for j in range(n): #x ax
        cnt = 0
        for k in range(4):
            nx = j +dxs[k]
            ny = i + dys[k]
            if in_range(nx,ny,n) and arr[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            cnt1+=1
print(cnt1)
# for x,y in zip(n,n): 
#     cnt = 0
#     for dx, dy in zip(dxs, dys):
#         nx, ny = x + dx, y + dy
#         if in_range(nx, ny) and arr[nx][ny] == 1:
#             cnt += 1
#     if cnt >= 3:
#         cnt1 += 1
# print(cnt1)