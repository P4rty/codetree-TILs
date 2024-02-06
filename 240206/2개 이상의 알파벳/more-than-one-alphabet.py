def alphabet_count(A):
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            print('Yes')
            return
    print('No')
A = list(input())
alphabet_count(A)