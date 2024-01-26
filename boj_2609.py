a, b = map(int, input().split())
prime_list = []
for num in range(2, 10001):
    cnt = 2
    while cnt < num:
        if num % cnt == 0:
            break
        else:
            cnt += 1
    if cnt == num:
        prime_list.append(num)

min_num = min(a, b)
i = 0
answer = 1
while prime_list[i] <= min_num:
    if a % prime_list[i] == 0 and b % prime_list[i] == 0:
        a = a // prime_list[i]
        b = b // prime_list[i]
        answer *= prime_list[i]
    else:
        i += 1
    
answer2 = answer * a * b
print(answer, answer2, sep='\n')
