n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
max_time = 0
for fired_person in range(n):
    time_lst = [0] * 1001
    cur_x = [a[j] for j in range(n) if j != fired_person]
    cur_y = [b[j] for j in range(n) if j != fired_person]
    for i in range(n-1):
        for k in range(cur_x[i], cur_y[i]):
            if time_lst[k] != 0:
                continue
            else:
                time_lst[k] = 1
    time = 0
    for l in range(1001):
        if time_lst[l] == 1:
            time += 1
    if max_time < time:
        max_time = time

print(max_time)



    