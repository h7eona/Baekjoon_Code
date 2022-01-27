n = int(input())

if n < 100:
    count = n
else:
    count = 99
    for i in range(100 , n + 1):
        i_list = list(map(int, str(i)))
        if i_list[1] - i_list[0] == i_list[2] - i_list[1]:
            count += 1

print(count)