def prnt(n):
    if n==0:
        return
    
    prnt(n-1)
    print("HelloWorld")
    
N = int(input())
prnt(N)