import sys
from collections import deque

N = int(input())

ans = deque([])
for i in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
       ans.append(order[1]) 
    if order[0] == 'front':
        if len(ans) > 0:
            print(ans[0])
        else:
            print(-1)
    if order[0] == 'back':
        if len(ans) > 0:
            print(ans[-1])
        else:
            print(-1)
    if order[0] == 'size':
        print(len(ans))
    if order[0] == 'empty':
        if len(ans) > 0:
            print(0)
        else:
            print(1)
    if order[0] == 'pop':
        if len(ans) > 0:
            print(ans.popleft())
            
        else:
            print(-1)
