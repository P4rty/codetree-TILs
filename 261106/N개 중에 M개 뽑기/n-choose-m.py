N, M = map(int, input().split())
visited = [False] * (N + 1)
# Please write your code here.
out = []

def backtracking(depth,start):
  if depth == M:
    print(' '.join(map(str, out)))
    return

  for i in range(start, N + 1):
    out.append(i)
    backtracking(depth + 1, i + 1)
    out.pop()

backtracking(0, 1)