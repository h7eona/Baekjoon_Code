num_list = list(map(int, input().split()))
n1, n2 = '', ''
for i in range(len(num_list)):
    if i == 0 or i == 1:
        n1 += str(num_list[i])
    else:
        n2 += str(num_list[i])
        
result = int(n1) + int(n2)
print(result)
