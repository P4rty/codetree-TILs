n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dir = {
    'L' : 0,
    'R' : 1,
    'U' : 2,
    'D' : 3,
}
move_dir = dir[d]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
r , c = r - 1, c - 1
for i in range(t):
    # t초  동안 움직일껀데,
    # 방향 바뀌는 데 1초 걸림
    #  방향은 위 아래만, 오 왼만
    nr , nc = r + dr[move_dir], c + dc[move_dir]
    if not(0 <= nr < n and 0 <= nc < n):
        if move_dir == 0:
            move_dir = 1
        elif move_dir == 1:
            move_dir = 0
        elif move_dir == 2:
            move_dir = 3
        elif move_dir == 3:
            move_dir = 2
    else:
        r, c  = nr, nc

print(r + 1, c + 1)


