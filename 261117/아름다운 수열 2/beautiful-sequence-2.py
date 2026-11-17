N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = 0
sorted_B = sorted(B)
for i in range(N - M + 1):
    sub_A = sorted(A[i : i + M])
    if sub_A == sorted_B:
        ans += 1
print(ans)
    
        
