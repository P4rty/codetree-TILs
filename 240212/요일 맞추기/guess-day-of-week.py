def day_of_week(m, d):
    # 2011년 1월 1일은 토요일이므로, 토요일을 0으로 기준으로 요일을 계산
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = (m - 1) * 31 + d - 1

    return total_days

m1, d1, m2, d2 = map(int, input().split())


start_day = day_of_week(m1, d1)


target_day = day_of_week(m2, d2)

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri","Sat", "Sun"]
f = (target_day-start_day)%7
print(days_of_week[f])