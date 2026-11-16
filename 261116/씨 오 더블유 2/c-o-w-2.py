n = int(input())
S = input()

# Please write your code here.
cnt = 0
for i in range(n - 2):
    for j in range(1, n - 1):
        for k in range(2, n):
            if i< j and j < k:
                if S[i] == 'C' and S[j] == 'O' and S[k] == 'W':
                    cnt += 1
print(cnt)