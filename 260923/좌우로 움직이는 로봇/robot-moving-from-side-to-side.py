n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# 로봇 A의 이동을 리스트에 담자.
a_loc = [0]
sec = 0
for i in range(n):
    if d[i] == 'L':
        # 왼쪽
        for _ in range(t[i]):
            sec -= 1
            a_loc.append(sec)
    else: # 오른쪽
        for _ in range(t[i]):
            sec += 1
            a_loc.append(sec)
b_loc = [0]
sec = 0
for i in range(m):
    if d_b[i] == 'L':
        # 왼쪽
        for _ in range(t_b[i]):
            sec -= 1
            b_loc.append(sec)
    else: # 오른쪽
        for _ in range(t_b[i]):
            sec += 1
            b_loc.append(sec)

max_len = max(len(a_loc), len(b_loc))

while len(a_loc) < max_len:
    a_loc.append(a_loc[-1])

while len(b_loc) < max_len:
    b_loc.append(b_loc[-1])

cnt = 0

for i in range(1, max_len):
    # 직전(i-1)에는 위치가 달랐고, 현재(i)에는 위치가 같은 경우만 카운트
    if a_loc[i-1] != b_loc[i-1] and a_loc[i] == b_loc[i]:
        cnt += 1

print(cnt)
# if len(a_loc) >= len(b_loc): # a 가 더 오래 돈 경우
#     for i in range(len(a_loc)):
#         if i >= len(b_loc):
#             if a_loc[i] == b_loc[-1] and a_loc[i] == b_loc[i-1]:
#                 cnt += 1
#         else:
#             if a_loc[i] == b_loc[i]:
#                 cnt += 1
# else:
#     for i in range(len(b_loc)):
#         if i >= len(a_loc):
#             if b_loc[i] == a_loc[-1]:
#                 cnt += 1
#         else:
#             if a_loc[i] == b_loc[i]:
#                 cnt += 1