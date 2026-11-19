T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
cnt = 0
for i in range(a, b + 1):
    d1,d2 = 1001, 1001
    for j in range(T):
        if c[j] == 'S':
            d1 = min(d1, abs(x[j] - i))
        elif c[j] == 'N':
            d2 = min(d2, abs(x[j] - i))
    if d1 <= d2:
        cnt += 1

print(cnt)