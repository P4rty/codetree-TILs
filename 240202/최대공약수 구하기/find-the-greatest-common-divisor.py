import sys

def input():
    return sys.stdin.readline().rstrip()
def gcdd (n,m):
    for i in range(2,n):
        if n%i == 0 and m%i ==0:
            gcd = i
    print(gcd)



n,m = map(int,input().split())
gcdd(n,m)