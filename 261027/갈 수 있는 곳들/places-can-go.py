from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
dr = [1, 0 , -1 ,0]
dc = [0, -1, 0 , 1]
visited = [[0]*n for _ in range(n)]

q = deque()
cnt = 0
for i in range(k):
    r, c  = points[i]
    r -= 1
    c -= 1
    q.append((r, c))
    visited[r][c] = 1
    cnt += 1


while q:
    r, c = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and visited[nr][nc] == 0:
            cnt += 1
            visited[nr][nc] += 1
            q.append((nr, nc))
print(cnt)