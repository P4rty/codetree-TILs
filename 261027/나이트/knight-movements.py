from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

dr = [2, 1, 2, 1, -2, -1, -2, -1]
dc = [1, 2, -1, -2, 1, 2, -1, -2]

q = deque([(r1, c1)])
visited = [[-1] * n for _ in range(n)]
visited[r1][c1] = 0

while q:
    r, c = q.popleft()
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr,nc))
print(visited[r2][c2])