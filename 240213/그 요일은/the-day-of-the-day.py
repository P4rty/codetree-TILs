days_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1,d1,m2,d2 = map(int,input().split())
A = input()

def num_of_days(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]
    
    total_days += d
    
    return total_days    

total_days_start = num_of_days(m1, d1)
total_days = (num_of_days(m2, d2) - num_of_days(m1, d1))
total_week = total_days //7 +1
start_day_index = days_week.index(A)

occurrences = total_week+ (start_day_index <= (total_days_start % 7))
print(occurrences)