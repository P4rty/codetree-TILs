Ai,Bi = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idx_a = 0
idx_b = 0

while idx_a < Ai and idx_b < Bi:
    if A[idx_a] == B[idx_b]:
        idx_b += 1
    idx_a += 1
    
    

if idx_b == Bi :
    print("Yes")
else:
    print("No")