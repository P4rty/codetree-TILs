def is_yoon(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def month_check(t,M,D):
    if t :
        if M == 2:
            if 1 <= D <=29:
                return True
            else:
                return False
        if M in (1,3,5,7,8,10,12):
            if 1 <= D <= 31:
                return True
            else:
                return False
        elif M in (4, 6, 9, 11):
            if 1 <= D <= 30:
                return True
            else:
                return False
    else:
        if M == 2:
            if 1 <= D <= 28:
                return True
        else:
            return False
        if M in (1,3,5,7,8,10,12):
            if 1 <= D <= 31:
                return True
            else:
                return False
        elif M in (4, 6, 9, 11):
            if 1 <= D <= 30:
                return True
            else:
                return False
def is_season(t,M):
    if t == 1:
        if M in (3,4,5):
            print('Spring')
        if M in (6,7,8):
            print('Summer')
        if M in (9,10,11):
            print('Fall')
        if M in (12,1,2):
            print('Winter')
    else:
        print("-1")

Y,M,D = map(int,input().split())
is_season(month_check(is_yoon(Y),M,D),M)