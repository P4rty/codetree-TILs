import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = []
for i in range(N):
    S = input()
    if S.startswith('push_back'):
        _, c = S.split(' ')
        stack.append(int(c))
    if S == 'pop_back':
        c = stack.pop()

    if S == 'size':
        print(len(stack))

    if S.startswith('get'):
        _, c = S.split(' ')
        print(stack[int(c)-1])