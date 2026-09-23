import sys
# 재귀 호출 한도 늘리기 (필요 시)
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, 0], [0, 1]
visited = [[False for _ in range(m)] for _ in range(n)]

def can_go(x, y):

    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    visited [x][y] = True

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y+ dy
        if can_go(new_x, new_y):
            dfs(new_x,new_y)



visited[0][0] = True
dfs(0,0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)

 