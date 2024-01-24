arr= list(map(int,input().split()))
arr_ch = []
for i in range (len(arr)):
    if arr[i] != 0 :
        if (arr[i]//10) !=0 :
            arr_ch.append(arr[i] // 10)
    else:
        break
count_arr = [0]*9

for element in arr_ch:
    count_arr[element-1] +=1

for i in range(9):
    print(f'{i+1} - {count_arr[i]}')