n=int(input())
arr= list(map(int,input().split()))
count_arr = [0]*9
for element in arr:
    count_arr[element-1] +=1

for i in range(9):
    print(count_arr[i])