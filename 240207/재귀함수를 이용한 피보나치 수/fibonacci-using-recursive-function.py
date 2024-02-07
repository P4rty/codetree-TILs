def pibonazi(n):
    if n == 1:
        return 1 
    
    if n == 2:
        return 1
    return pibonazi(n-1)+ pibonazi(n-2)

N = int(input())
print(pibonazi(N))