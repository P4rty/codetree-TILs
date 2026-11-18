N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P = sorted(P)
# Please write your code here.
students = 0
for sale in range(N):
    check_price = B
    count = 0
    for i in range(N):

        if i == sale:
            price = P[i]/2
        else:
            price = P[i]
        if check_price < price:
            break
        check_price -= price
        count += 1
    if count > students:
        students = count
print(students)
        