A = input()
B = input()
cnt = 0
check = 0
while cnt<len(A):
    A = A[-1]+A[0:-1]
    if A == B:
        cnt = cnt + 1
        check = 1
        break
    else:
        cnt = cnt + 1

if check ==1:
    print(cnt)
else:
    print(-1)