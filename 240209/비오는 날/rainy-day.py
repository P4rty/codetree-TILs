class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
        
users = []
n = int(input())
for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        users.append(Forecast(date, day, weather))

slowest_person = min(users, key=lambda x: x.date)

print("{0} {1} {2}".format(slowest_person.date, slowest_person.day,slowest_person.weather))