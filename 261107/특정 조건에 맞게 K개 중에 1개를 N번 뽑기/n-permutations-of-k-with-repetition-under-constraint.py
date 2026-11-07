K, N = map(int, input().split())

# Please write your code here.
ans = []

def permut(cnt):
    if cnt == N:
        print(*ans)
        return
    
    for i in range(1, K + 1):
        if cnt >= 2 and ans[-1] == i and ans[-2] == i:
            continue
        ans.append(i)
        permut(cnt + 1)
        ans.pop()

permut((0))