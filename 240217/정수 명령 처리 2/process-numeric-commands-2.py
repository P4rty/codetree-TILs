from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

queue1 = deque()
n = int(input())
for _ in range(n):
    command = input()
    if command.startswith("push"):
        _, c =command.split(" ")
        queue1.append(c)
    elif command == 'pop':
        if queue1:
            a= queue1.popleft()
            print(a)
    elif command == 'size':
        print(len(queue1))
    elif command == 'empty':
        if queue1:
            print(0)
        else:
            print(1)
    elif command == 'front':
        print(queue1[0])