from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
# Please write your code here.
dist = [[-1]* m for _ in range(n)]
dist[0][0] = 1
q = deque([(0, 0)])

while q:
    r, c = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1 and a[nr][nc] != 0:
            dist[nr][nc] = 1
            q.append((nr,nc))
if dist[n-1][m-1] != -1:
    print(1)
else:
    print(0)
