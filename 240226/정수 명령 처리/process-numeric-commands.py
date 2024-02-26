import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = []

for i in range(N):
    q = input()
    if q.startswith('push'):
        _, c = q.split(' ')
        stack.append(int(c))
    if q == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            c = stack.pop()
            print(c)
    if q == 'size':
        print(len(stack))
    if q == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if q == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])