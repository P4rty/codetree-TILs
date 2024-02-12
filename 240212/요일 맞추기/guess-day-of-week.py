days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())


start_day = 0
elapsed_days = 0
if m1< m2:
    while True:
        if m1 == m2 and d1 == d2:
            break

        elapsed_days += 1
        d1 += 1

        if d1 > num_of_days[m1]:
            m1 += 1
            d1 = 1
else:
     while True:
        if m1 == m2 and d1 == d2:
            elapsed_days -=1
            break

        elapsed_days -= 1
        d1 -= 1

        if d1 ==1:
            m1 -= 1
            d1 = num_of_days[m1]

f = elapsed_days % 7


print(days_of_week[f])