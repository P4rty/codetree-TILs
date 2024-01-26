def is_subsequence(n1, n2, sequence_a, sequence_b):
    # 수열 A의 모든 원소에 대해 순차적으로 탐색
    for i in range(n1):
        # 수열 B의 현재 원소가 수열 A의 현재 원소와 같으면
        if sequence_b[0] == sequence_a[i]:
            # 수열 B의 나머지 원소가 순서대로 수열 A와 일치하는지 확인
            j = 1
            while j < n2 and i + j < n1 and sequence_b[j] == sequence_a[i + j]:
                j += 1
            
            # 수열 B의 모든 원소가 일치하면 연속부분수열이므로 "Yes" 반환
            if j == n2:
                return "Yes"

    # 수열 B의 어떤 부분도 연속부분수열이 아닌 경우 "No" 반환
    return "No"

# 입력 받기
n1, n2 = map(int, input().split())
sequence_a = list(map(int, input().split()))
sequence_b = list(map(int, input().split()))

# 결과 출력
result = is_subsequence(n1, n2, sequence_a, sequence_b)
print(result)