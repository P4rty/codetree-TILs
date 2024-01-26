numbers = list(map(int, input().split()))

max_number = float('-inf')  # 가장 작은 값으로 초기화
min_number = float('inf')   # 가장 큰 값으로 초기화

for num in numbers:
    if num == 999 or num == -999:
        break
    
    # 현재 입력된 숫자가 최대값 또는 최소값인지 확인
    max_number = max(max_number, num)
    min_number = min(min_number, num)

# 최대값과 최소값 출력
print(max_number, min_number)