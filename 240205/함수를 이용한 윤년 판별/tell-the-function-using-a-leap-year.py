def is_yoonnun(n):
    if n % 4 == 0:
        return True
    elif n % 4 == 0 and n % 100 == 0:
        return False
    elif n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        return True
    return False

y = int(input())
if y:
    print('true')
else:
    print('false')