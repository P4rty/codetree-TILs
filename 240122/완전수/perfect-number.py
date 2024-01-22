start, end = map(int, input().split())
cnt = 0
sum1 = 0

for i in range(start, end + 1):
    for j in range(1, i):
        if i % j == 0:
            sum1 += j
    if sum1 == i:
        cnt += 1
    sum1 = 0

print(cnt)