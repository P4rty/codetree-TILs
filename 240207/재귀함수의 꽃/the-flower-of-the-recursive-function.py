n= int(input())

def tntwk(n):
    if n == 0:
        return
    print(n,end=" ")
    tntwk(n-1)
    print(n,end=" ")


tntwk(n)