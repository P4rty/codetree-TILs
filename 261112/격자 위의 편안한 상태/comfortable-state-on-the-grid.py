n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
board = [[0]* n for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for command in range(m):
    r, c = points[command]
    r, c = r - 1, c - 1
    board[r][c] = 1
    cnt = 0
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 0:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
