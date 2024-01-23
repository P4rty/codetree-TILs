arr = list(map(int, input().split()))
sum1=0
sum2=0
for i in range(0,10,2):
    sum1+=arr[i]

for i in range(0,10,3):
    sum2 +=arr[i]

print('{0} {1:.1f}'.format(sum1 ,sum2/3))