n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# V = n, E = m
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i, j in edges:
    graph[i][j] = 1
    graph[j][i] = 1

S = 1
stack = [S]
visited = [False]*(n+1)
visited[S] = True

while stack:
    curr = stack.pop()

    for nxt in range(1, n+1):
        if graph[curr][nxt] == 1 and not visited[nxt]:
            visited[nxt] = True
            stack.append(nxt)
print(sum(visited)-1)