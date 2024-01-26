arr = list(map(int,input().split()))
barr=[]#500초과의 수
aarr=[]# 500미만의 수
for i in range(10):
    if arr[i]>500:
        barr.append(arr[i])
    else:
        aarr.append(arr[i])

print(f'{max(aarr)} {min(barr)}')