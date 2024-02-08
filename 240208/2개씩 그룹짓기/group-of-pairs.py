N = int(input())
num_2N = list(map(int,input().split()))
num_2N.sort()
print(num_2N[N+1]+num_2N[N-1])