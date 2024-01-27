avg=list()
avg_rk1 =0
avg_rk2=0
avg_tp1=0
avg_tp2=0
avg_tp3=0
avg_tp4=0
for i in range(2):
    arr = list(map(int,input().split()))
    avg.append(arr)
for j in range(4):
    avg_rk1+=avg[0][j]
    avg_rk2+=avg[1][j]
avg_rk1 = avg_rk1 /4
avg_rk2 = avg_rk2 /4
print('{0:.1f} {1:.1f}'.format(avg_rk1,avg_rk2))
for k in range(2):
    avg_tp1 += avg[k][0]
    avg_tp2 += avg[k][1]
    avg_tp3 += avg[k][2]
    avg_tp4 += avg[k][3]
avg_tp1 /=2
avg_tp2 /=2
avg_tp3 /=2
avg_tp4 /=2
print('{0:.1f} {1:.1f} {2:.1f} {3:.1f}'.format(avg_tp1,avg_tp2,avg_tp3,avg_tp4))
akk = (avg_rk1+avg_rk2)/2
print('{0:.1f}'.format(akk))