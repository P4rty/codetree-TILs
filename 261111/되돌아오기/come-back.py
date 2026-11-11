N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
time = 0

direction = {
    "N" : 0,
    "E" : 1,
    "S" : 2,
    "W" : 3,
}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c = 0, 0
ans = [] 
for i in range(N):
    for j in range(dist[i]):
        time += 1
        curr_dir = direction[dir[i]]
        r, c = r + dr[curr_dir], c + dc[curr_dir]
        if r == 0 and c == 0:
            ans.append(time)

        
        
if ans:
    print(ans[0])
else:
    print(-1)