import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
# Please write your code here.
dr = [1, 0 , -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]
    
    dp[r][c] = 1
    
        
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    
    return dp[r][c]

max_len = 0
for r in range(n):
    for c in range(n):
        max_len = max(max_len, dfs(r, c))
print(max_len)
