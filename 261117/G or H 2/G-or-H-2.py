n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
arr = [0] * 101
for pos_str, char in people:
    arr[int(pos_str)] = char
max_cnt = 0
for i in range(101):
    for j in range(i, 101):
        if arr[i] == 0 or arr[j] == 0:
            continue
        g_count = 0
        h_count = 0
        people_count = 0

        for k in range(i, j + 1):
            if arr[k] == 'G':
                g_count += 1
                people_count += 1
            elif arr[k] == 'H':
                h_count += 1
                people_count += 1
        if people_count == 0:
            continue
        if people_count == 1 or g_count == 0 or h_count == 0 or g_count == h_count:
            max_cnt = max(max_cnt, j - i)
print(max_cnt)