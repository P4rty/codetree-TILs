n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B)

if A == B :
    print("Yes")
else:
    print("No")