def is_prime(n):
    for j in range(2,n):
        if n % j ==0:
            return False
    return True
temp = 0 
a,b = map(int,input().split())
for i in range(a,b):
    k = is_prime(i)
    if k == True:
        temp += i

print(temp)