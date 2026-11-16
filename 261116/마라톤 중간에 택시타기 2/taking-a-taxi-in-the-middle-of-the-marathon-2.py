n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
min_distance = float("inf")
# Please write your code here.
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# n번 반복하며, n 번째 때 빠진다고 생각.
for skip_idx in range(1, n-1):
    check_distance = 0
    prev_idx = 0

    for i in range(1,n):
        if i == skip_idx:
            continue
        check_distance += manhattan(points[prev_idx],points[i])
        prev_idx = i

    if check_distance < min_distance:
        min_distance = check_distance
print(min_distance)