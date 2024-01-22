given_arr = input().split()
arr = []

for i in given_arr:
    arr.append(int(i))

result_arr = []
for val in arr:
    if val < 250:
        result_arr.append(val)
    else:
        break

sum_val = sum(result_arr)
avg = sum_val / len(result_arr) if len(result_arr) > 0 else 0

print('{0} {1:.1f}'.format(sum_val, avg))