N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
ans = -1
for i in range(N - 1):
    for j in range(i + 1, N):
        if num[i] == num[j] and abs(i - j) <= K:
            if num[i] > ans:
                ans = num[j]

print(ans)


