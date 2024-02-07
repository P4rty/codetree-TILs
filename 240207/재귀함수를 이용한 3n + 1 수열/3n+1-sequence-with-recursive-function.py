def f(n,cnt):
    if n == 1 :
        return cnt
    elif n % 2 ==0:
        n = n//2
        cnt += 1
        return f(n,cnt)
    elif n % 2 == 1:
        n = n*3+1
        cnt += 1
        return f(n,cnt)
        
n= int( input())
cnt = 0
print(f(n,cnt))