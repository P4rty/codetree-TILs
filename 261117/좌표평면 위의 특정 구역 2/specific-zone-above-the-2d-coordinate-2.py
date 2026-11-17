n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_area = float("inf")
for i in range(n):
    cur_x = [points[j][0] for j in range(n) if j != i]
    cur_y = [points[j][1] for j in range(n) if j != i]

    width = max(cur_x) - min(cur_x)
    height = max(cur_y) - min(cur_y)
    area = width * height
    min_area = min(min_area, area)

print(min_area)