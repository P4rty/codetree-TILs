def is_yoonnun(n):
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
y = int(input())
if y:
    print('true')
else:
    print('false')