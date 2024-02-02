def find369(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i % 3 ==0:
            cnt += 1
        elif i%10 == 3 or i % 10 == 6 or i% 10 == 9:
            cnt += 1
        elif i//10 == 3 or i//10 == 6 or i//10 == 9:
            cnt += 1
        elif i//100 == 3 or i//100 == 6 or i//100 == 9:
            cnt+=1
        elif i//1000 == 3 or i//1000 == 6 or i//1000 == 9:
            cnt+=1
        elif i//10000 == 3 or i//10000 == 6 or i//10000 == 9:
            cnt+=1
        
    return cnt
a,b = map(int,input().split())
print(find369(a,b))