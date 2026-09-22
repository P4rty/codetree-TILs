n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
trominos = [
    ((0, 1, 1), (0, 0, 1)), # ㄱ
    ((0, 0, 1), (0, 1, 1)), # ㄴ
    ((0, 1, 0), (0, 0, 1)), # 역 ㄱ
    ((0, 1, 1), (1, 0, 1)), # 역 ㄴ
    ((0, 1, 2), (0, 0, 0)), # - 
    ((0, 0, 0), (0, 1, 2)) # |

]

possiblesum = list()

for r in range(n):
    for c in range(m):
        for drlist, dclist in trominos:
            # 한 r, c 마다 확인.
            cnt = 0
            for dr, dc in zip(drlist,dclist):
                nxtr, nxtc = r+dr, c+dc
                if 0 <= nxtr <n and 0 <= nxtc < m:
                    cnt += grid[nxtr][nxtc]
                else:
                    break
            else:
                possiblesum.append(cnt)


print(max(possiblesum))