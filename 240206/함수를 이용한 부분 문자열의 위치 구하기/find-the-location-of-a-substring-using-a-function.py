def find_substring_index(input_str, target_str):
    len_input = len(input_str)
    len_target = len(target_str)

    # 목적 문자열이 입력 문자열보다 길면 부분 문자열이 될 수 없으므로 -1을 반환합니다.
    if len_target > len_input:
        return -1

    # 입력 문자열을 순회하면서 목적 문자열이 부분 문자열로 존재하는지 확인합니다.
    for i in range(len_input - len_target + 1):
        if input_str[i:i + len_target] == target_str:
            return i

    # 목적 문자열이 부분 문자열로 존재하지 않는 경우 -1을 반환합니다.
    return -1

# 입력을 받습니다.
input_str = input()
target_str = input()

# 함수를 호출하여 부분 문자열의 시작 인덱스를 출력합니다.
result = find_substring_index(input_str, target_str)
print(result)