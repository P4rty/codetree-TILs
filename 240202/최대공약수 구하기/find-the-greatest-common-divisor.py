def gcdd (n,m):
    for i in range(2,n):
        if n%i == 0 and m%i ==0:
            gcd = i
    return gcd



n,m = map(int,input().split())

print(gcdd(n,m))