R,C = map(int,input().split())#R - 세로 C - 가로
arr = [ input().split() for _ in range(R)]
x,y = 0,0
cnt = 0
if arr[0][0] == arr[R-1][C-1]:
    print(0)
else:
    for i in range(R-1):
        for j in range(C-1):
            if arr[0][0] != arr[i][j]:# 처음 점프 할 곳 찾음
                for k in range(i+1,R-1):
                    for l in range(j+1,C-1):
                        cnt += 1 #다음점프?
    print(cnt)