n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
two_sum = 0
for i in range(n):
    check = 0
    for j in range(n - 2):
        if abs(i - j) >= 2:
            check = numbers[i]+ numbers[j]

        if two_sum < check:
            two_sum = check
print(two_sum)
