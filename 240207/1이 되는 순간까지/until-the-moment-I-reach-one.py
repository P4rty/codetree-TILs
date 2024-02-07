def f(n,cnt):
    if n == 1:
        return cnt
    elif n % 2 == 0:
        n= n//2
        return f(n,cnt+1)
    else :
        n = n//3
        return f(n,cnt+1)



N = int(input())
cnt = 0
print(f(N,cnt))