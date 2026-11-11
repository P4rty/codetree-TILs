n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c = 0, 0
d = 0
for k in range(n*m):
    arr[r][c] = k + 1
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
        r, c = nr, nc
    
    else:
        d = (d + 1) % 4
        r, c = r + dr[d], c + dc[d]

for r in range(n):
    for c in range(m):
        print(arr[r][c], end = " ")
    print()
