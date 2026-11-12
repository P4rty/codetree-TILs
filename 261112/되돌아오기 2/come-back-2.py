commands = input()

# Please write your code here.
# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direction = 0
r, c = 0, 0
time = 0
for command in commands:
    if command == "L":
        direction = (direction + 3) % 4
    elif command == "R":
        direction = (direction + 1) % 4
    elif command == "F":
        r, c = r + dr[direction], c + dc[direction]
    time += 1
    if r == 0 and c == 0:
        print(time)
        break
else:
    print(-1)
