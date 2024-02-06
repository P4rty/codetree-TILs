def is_subsequence(n1, n2, A, B):
    if n2 > n1:
        return "No"
    for i in range(n1 - n2 + 1):
        if A[i:i+n2] == B:
            return "Yes"
    return "No"
    
n1, n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(is_subsequence(n1,n2,A,B))