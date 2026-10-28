n = int(input())

memo = [-1 for _ in range(n+1)]

def dp(n):
    if memo[n] != -1:
        return memo[n]
    
    if n == 1 or n == 0:
        memo[n] = 0
    elif n == 2 or n == 3:
        memo[n] = 1
    else:
        memo[n] = dp(n - 2) + dp(n - 3)
    return memo[n]
answer = dp(n) % 10007
print(answer)