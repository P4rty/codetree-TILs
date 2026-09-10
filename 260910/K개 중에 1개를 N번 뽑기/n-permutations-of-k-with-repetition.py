K, N = map(int, input().split())
answer = []
# Please write your code here.
def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()
def choose(curr_num):
    # 종료 조건
    if curr_num == N + 1:
        print_answer()
        return
    # 재귀 호출
    for i in range(1, K+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()

choose(1)

