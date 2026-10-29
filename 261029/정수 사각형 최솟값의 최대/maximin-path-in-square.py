n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0]*n for _ in range(n)]
dp[0][0] = grid[0][0]

for r in range(1,n):
    dp[r][0] = min(dp[r-1][0], grid[r][0])
for c in range(1,n):
    dp[0][c] = min(dp[0][c-1], grid[0][c])
for r in range(1, n):
    for c in range(1, n):
        dp[r][c] = min(max(dp[r-1][c], dp[r][c-1]), grid[r][c])
print(dp[n - 1][n - 1])