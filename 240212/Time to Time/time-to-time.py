hour, mins, dh , dm =map(int,input().split())
elapsed_time = 0

while True:
    if hour == dh and mins == dm:
        break

    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(elapsed_time)