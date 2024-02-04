def is_prime(n):
    if n == 1 :
        return False
    for j in range(2,n):
        if n % j ==0:
            return False
    return True
temp = 0 
a,b = map(int,input().split())
for i in range(a,b+1):
    k = is_prime(i)
    if k == True:
        temp += i

print(temp)