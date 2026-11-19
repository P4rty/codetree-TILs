X, Y = map(int, input().split())
ans = 0
# Please write your code here.
for num in range(X, Y + 1):
    s = str(num)
    length = len(s)
    is_interesting = False
    for digit in range(10):
        # 특정 숫자가 (전체 자릿수 - 1)번 등장했다면 나머지 한 자리는 자동으로 다른 숫자임
        if s.count(str(digit)) == length - 1:
            is_interesting = True
            break
            
    if is_interesting:
        ans += 1
print(ans)