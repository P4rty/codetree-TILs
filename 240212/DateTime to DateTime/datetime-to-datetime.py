a, b, c = map(int, input().split())
start_time = (11, 11, 11)
target_time = (a, b, c)

start_minutes = start_time[0] * 24 * 60 + start_time[1] * 60 + start_time[2]
target_minutes = target_time[0] * 24 * 60 + target_time[1] * 60 + target_time[2]


elapsed_minutes = target_minutes - start_minutes
print(elapsed_minutes)