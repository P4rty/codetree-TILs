A = input()
quest = input()

for i in range(len(quest)):
    if quest[i]=='L':
        A = A[1:]+A[0]
    elif quest[i] == 'R':
        A = A[-1]+A[:-1]
print(A)