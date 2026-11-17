n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


def sub(a, b, c):
    return abs((x[a] * y[b] + x[b] * y[c] + x[c] * y[a]) - (x[b] * y[a] + x[c] * y[b] + x[a] * y[c]))
ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            # 한변이 x축에 평행, 한변이 y축 에 평행
            if (x[i] == x[j] or x[j] == x[k] or x[k] == x[i]) and (y[i] == y[j] or y[j] == y[k] or y[k] == y[i]):
                ans = max (sub(i, j, k), ans)

print(ans)