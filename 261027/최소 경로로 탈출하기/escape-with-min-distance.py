n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
visited = [[-1]*m for _ in range(n)]

q = deque([(0,0)])
visited[0][0] = 0
dr = [1, 0, -1 ,0]
dc = [0, -1, 0 ,1]


while q:
    r, c = q.popleft()
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and a[nr][nc] != 0:
            
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr,nc))
            
print(visited[n-1][m-1])