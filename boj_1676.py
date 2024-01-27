n = int(input())

result = 1
if n == 0:
    result = 1
else:
    for i in range(n, 0, -1):
        result *= i

num_list = list(str(result))

cnt = 0
for i in range(len(num_list)-1, -1, -1):
    if num_list[i] == '0':
        cnt += 1
    else:
        break

print(cnt)


