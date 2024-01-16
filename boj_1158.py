N, K = map(int, input().split())

num_list = []
for i in range(1, N+1):
   num_list.append(i)
   
stack = []
ans = []

idx = 0
cnt = 1

while len(num_list) > 0:    
    stack.append(num_list[idx])

    if cnt % K == 0:
        ans.append(stack.pop())

    idx += 1
    cnt += 1
    
    if idx > len(num_list)-1:
        idx = 0
        num_list = stack.copy()
        stack = []
        
print('<', end='')
for t in ans:
    if t == ans[-1]:
        print(t, end='>')
    else:
        print(t, end=', ')
     
