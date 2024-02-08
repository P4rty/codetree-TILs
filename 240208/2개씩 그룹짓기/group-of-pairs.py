N = int(input())
num_2N = list(map(int,input().split()))
num_2N.sort()
f=[]
for i in range(N):
    f.append(num_2N[i]+num_2N[-1-i])
print(max(f))