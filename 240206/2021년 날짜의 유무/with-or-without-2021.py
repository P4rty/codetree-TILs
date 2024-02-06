def is_Day(M, D):
    if M in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= D <= 31:
            return True
        else:
            return False
    elif M in (4, 6, 9, 11):
        if 1 <= D <= 30:
            return True
        else:
            return False
    elif M == 2:
        if 1 <= D <= 28:
            return True
        else:
            return False

M, D = map(int, input().split())
if is_Day(M, D):
    print("Yes")
else:
    print("No")