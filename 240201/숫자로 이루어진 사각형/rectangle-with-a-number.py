def print_rect(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            if(cnt == 10): cnt =1
            print(cnt,end=" ")
            cnt+=1
        print()
N  = int(input())
print_rect(N)