n,m = map(int,input().split())
A = list(map(int,input().split()))

def fkfk(A,n,m):
    cnt = 0 
    while m>1:
        if m%2 ==0:
            cnt += A[m-1]
            m = m//2
        if m%2 ==1:
            cnt += A[m-1]
            m = m-1
    return cnt
print(fkfk(A,n,m))