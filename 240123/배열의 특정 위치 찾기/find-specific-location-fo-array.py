arr = list(map(int, input().split()))
sum1=0
sum2=0
for i in arr:
    if i%2==1:
        sum1+=arr[i]
    if (i+1)%3 ==0:
        sum2 +=arr[i]

print('{0} {1:.1f}'.format(sum1 ,sum2/3))