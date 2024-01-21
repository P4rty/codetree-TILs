n= int(input())

for i in range(1,n+1):
    for j in range(0,n):
        print(f'{10+2*i+2*j-1}',end=" ")
    print()