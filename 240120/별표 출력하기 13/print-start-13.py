n= int(input())

for i in range(1,2*n+1):
    if i%2 ==1:
        for j in range(int(0.5+n-0.5*i)):
            print("*",end=" ")

        print()

    if i%2 ==0:
        for j in range(i//2):
            print("*",end=" ")
            
        print()