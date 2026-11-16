n = int(input())
a = [int(input()) for _ in range(n)]
min_distance = float("inf")
# Please write your code here.
for start_idx in range(n):
    # n번 반복, 어디서 시작할지.
    check_distance = 0
    for i in range(n):
        if i >= start_idx:
            check_distance += a[i] * (i - start_idx)
        else:
            check_distance += a[i] * (n - start_idx + i)
    
    if min_distance > check_distance:
        min_distance = check_distance

print(min_distance)
    