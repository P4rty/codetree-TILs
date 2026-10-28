n = int(input())

memo = [-1 for _ in range(n+1)]


def dp(n):
    if memo [n] != -1:
        return memo[n]
    
    if n == 0:
        memo[n] = 0

    elif n == 1:
        memo[n] = 1
    elif n == 2:
        memo[n] = 2
    else:
        memo[n] = dp(n - 1) + dp(n - 2)    

    return memo[n]


answer = dp(n) % 10007
print(answer)