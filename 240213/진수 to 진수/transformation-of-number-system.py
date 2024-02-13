a,b = map(int,input().split())
n = input()
num  = 0
for i in range(len(n)):
    num = num*a+int(n[i])
n = num
num = []
while True:
    if n < b :
        num.append(n)
        break

    num.append(n % b)
    n = n // b

for num in num[::-1]:
    print(num, end="")