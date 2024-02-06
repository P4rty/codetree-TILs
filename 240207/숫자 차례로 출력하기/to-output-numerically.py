def tntwk1(n):
    if n == 0:
        return
    print(n,end=" ")
    tntwk1(n-1)

def tntwk(n):
    if n == 0:
        
        return
    tntwk(n-1)
    print(n,end=" ")
 

n= int(input())

tntwk(n)
print()
tntwk1(n)