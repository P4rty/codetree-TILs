def f(n):
    if n == 1:
        return 1
    if n ==2 :
        return 2 
    elif n % 2 == 0:
        return f(n-2)+n
    else:
        return f(n-2)+n
    

N = int(input())
print(f(N))