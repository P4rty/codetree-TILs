arr= list(map(int,input().split()))
count_arr = [0]*6
for element in arr:
    count_arr[element-1] +=1

for i in range(6):
    print(f'{i+1} - {count_arr[i]}')