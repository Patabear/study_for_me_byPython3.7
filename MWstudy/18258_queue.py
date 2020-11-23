from collections import deque
import sys

n = int(input())
que = deque()
size = int(0)

def empty():
    if size == 0:
        return 1
    else:
        return 0

command = []
for i in range(n):
    command.append(sys.stdin.readline().rstrip())

for com in command:
    arg = list(com.split())

    if arg[0] == "push":
        que.append(arg[1])
        size += 1
    
    elif arg[0] == "pop":
        if size != 0:
            print(que.popleft())
            size -= 1
        else:
            print(-1)
    
    elif arg[0] == "size":
        print(size)
    
    elif arg[0] == "empty":
        print(empty())
    
    elif arg[0] == "front":
        if size != 0:
            print(que[0])
        else:
            print(-1)
    
    elif arg[0] == "back":
        if size != 0:
            print(que[-1])
        else:
            print(-1)