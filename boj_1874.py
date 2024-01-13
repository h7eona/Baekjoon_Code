n = int(input())

num_list = []
for _ in range(1, n+1):
    num_list.append(int(input()))

num_list_tmp = list(reversed(num_list)).copy()

start = 1
push_list = []
ans = []
while start <= n:
    if len(push_list) > 0 and push_list[-1] == num_list_tmp[-1]:
        push_list.pop()
        num_list_tmp.pop()
        ans.append('-')
    else:
        push_list.append(start)
        ans.append('+')
        start += 1

while len(push_list) > 0:
    if push_list[-1] == num_list_tmp[-1]:
        push_list.pop()
        num_list_tmp.pop()
        ans.append('-')
    else:
        ans = ['NO']
        break

for k in ans:
    print(k)

