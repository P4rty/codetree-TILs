n,m = map(int,input().split())
A = list(map(int,input().split()))

def a1plusa2(n1,n2):
    global A
    return sum(A[n1-1:n2])

for _ in range(m):
    a1,a2 = map(int,input().split())
    print(a1plusa2(a1,a2))