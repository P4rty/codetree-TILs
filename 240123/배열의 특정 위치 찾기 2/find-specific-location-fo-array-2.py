arr1 = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(0,10,2):
    sum1 += arr1[i]
    
for i in range(1,10,2):
    sum2 += arr1[i]
print(abs(sum1-sum2))