def day_of_week(m, d):
    # 2011년 1월 1일은 토요일이므로, 토요일을 0으로 기준으로 요일을 계산
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = (m - 1) * 31 + d - 1

    for i in range(1, m):
        total_days -= days_in_month[i]

    day_of_week = (total_days + 6) % 7
    return day_of_week

# 입력값 받기
m1, d1, m2, d2 = map(int, input().split())

# 시작 날짜의 요일 계산
start_day = day_of_week(m1, d1)

# 목표 날짜의 요일 계산
target_day = (start_day + (d2 - d1)+3) % 7

# 요일 출력
days_of_week = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
print(days_of_week[target_day])