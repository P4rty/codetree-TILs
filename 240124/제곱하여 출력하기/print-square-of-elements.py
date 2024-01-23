n = int (input())
arr = list(input().split())
new_arr = []
for i in range(n):
    new_arr.append(int(arr[i])*int(arr[i]))
for j in range(n):
    print(new_arr[j],end= " ")