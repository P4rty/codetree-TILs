abilities = list(map(int, input().split()))

# Please write your code here.
sm = 0
for k in range(6):
    sm += abilities[k]

lr = len(abilities)
min_gap = float("inf")
teamsc = 0
for i in range(lr):
    for j in range(i + 1, lr):
        for k in range(j + 1, lr):
            min_gap = min(min_gap, abs(sm - 2*(abilities[i]+abilities[j]+abilities[k])))

print(min_gap)
