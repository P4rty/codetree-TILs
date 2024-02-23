# import sys
# def input():
#     return sys.stdin.readline()

# n = int(input())
# color_arrw = [0]*200001
# color_arrb = [0]*200001
# arrd = [0]*200001
# idx = 100000
# for i in range(n):
#     x,direction = map(str,input().split())
#     x = int(x)
#     if direction == "L":
#         for i in range(idx,idx-n,-1):
#             color_arrw[i] += 1
#             arrd[i] = 1
#         idx = idx - n + 1
#     else:
#         for i in range(idx,idx+n):
#             color_arrb[i] += 1
#             arrd[i] = 2 
#         idx = idx + n - 1

# cntb = 0
# cntw = 0
# cntg = 0


# for i in range(200001):

#     if color_arrb[i] >= 2 and color_arrw[i] >=2 :
#         cntg += 1
#     elif arrd[i] == 1 :
#         cntw += 1
#     elif  arrd[i] == 2 :
#         cntb += 1


# print(cntg, cntb, cntw)


MAX_K = 100000

n = int(input())
a = [0] * (2 * MAX_K + 1)
cnt_b = [0] * (2 * MAX_K + 1)
cnt_w = [0] * (2 * MAX_K + 1)
b, w, g = 0, 0, 0

cur = MAX_K

for _ in range(n):
    x, c = map(str, input().split())
    x = int(x)

    if c == 'L':
        # x칸 왼쪽으로 칠합니다.
        while x > 0:
            a[cur] = 1
            cnt_w[cur] += 1
            if x > 1:
                cur -= 1
            x -= 1
    else:
        # x칸 오른쪽으로 칠합니다.
        while x > 0:
            a[cur] = 2
            cnt_b[cur] += 1
            if x > 1:
                cur += 1
            x -= 1

for i in range(2 * MAX_K + 1):
    # 검은색과 흰색으로 두 번 이상 칠해진 타일은 회색입니다.
    if cnt_b[i] >= 2 and cnt_w[i] >= 2:
        g += 1
    # 그렇지 않으면 현재 칠해진 색깔이 곧 타일의 색깔입니다.
    elif a[i] == 1:
        w += 1
    elif a[i] == 2:
        b += 1

# 정답을 출력합니다.
print(w, b, g)