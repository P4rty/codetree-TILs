n,q = map(int,input().split())
arr = [0]*n
arr = list(map(int,input().split()))
for i in range(q):
    quest = []
    quest = list(map(int,input().split()))
    if quest[0] ==1:
        print (arr[quest[1]-1])

    elif quest[0] ==2:
        if quest[1] not in arr:
            print(0)
        else:
            print(arr.index(quest[1])+1)
    elif quest[0] == 3:
        for j in range(quest[1]-1,quest[1]+1):
            print(arr[j],end= " ")