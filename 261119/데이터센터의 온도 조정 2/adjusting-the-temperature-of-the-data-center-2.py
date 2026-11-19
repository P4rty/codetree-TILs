N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
work_max = 0

for j in range(-1, 1005):
    work = 0
    for ta, tb in ranges:
        if ta > j:
            work += C
        elif ta <= j <= tb:
            work += G
        elif tb < j:
            work += H
    work_max = max(work, work_max)

print(work_max)

