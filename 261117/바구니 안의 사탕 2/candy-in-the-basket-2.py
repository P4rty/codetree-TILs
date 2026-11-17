N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
max_candy = 0

for c in range(101):
    current_candy = 0
    for i in range(N):
        if c - K <= pos[i] <= c + K:
            current_candy += candy[i]
    
    if current_candy > max_candy:
        max_candy = current_candy

print(max_candy)