n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]* n for _ in range(n)]
dp[0][n-1] = grid[0][n-1]

for r in range(1, n):
    dp[r][n - 1] = dp[r - 1][n - 1] + grid[r][n - 1]
for c in range(n-2, -1, -1):
    dp[0][c] = dp[0][c + 1] + grid[0][c]

for r in range(1, n):
    for c in range(n - 2, -1, -1):
        dp[r][c] = min(dp[r - 1][c]+grid[r][c], dp[r][c + 1]+grid[r][c])

print(dp[n-1][0])