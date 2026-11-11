n = int(input())

# Please write your code here.

ans = []
cnt = 0
def perm(curr_num):
    global cnt
    if curr_num == n:
        cnt += 1
        return
    
    if curr_num > n:
        return

    #  재귀 호출
    for i in range(1, 5):
        if curr_num + i > n + 1:
            continue
        for _ in range(i):
            ans.append(i)
        
        perm(curr_num+i)
        for _ in range(i):
            ans.pop()

perm(0)
print(cnt)

