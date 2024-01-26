# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 숫자들의 등장 횟수를 세는 함수 정의
def count_occurrences(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

# 숫자들의 등장 횟수 계산
occurrences = count_occurrences(numbers)

# 중복하지 않는 숫자 중 최댓값 찾기
max_unique_number = max((num for num, count in occurrences.items() if count == 1), default=-1)

# 결과 출력
print(max_unique_number)