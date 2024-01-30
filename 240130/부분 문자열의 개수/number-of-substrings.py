A = input()
B = input()
len_a= len(A)
len_b = len(B)
exists = False
cnt_b = 0
for i in range(len_a - len_b+1):
    cnt = 0
    for j in range(len_b):
        if A[i+j] == B[j]:
            cnt +=1

        if A[i+j] != B[j]:
            exists = False
    if cnt == len_b:
        exists = True
        cnt_b +=1
if exists == True:
    print(cnt_b)