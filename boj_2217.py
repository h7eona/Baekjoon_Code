N = int(input())
weight_list = []
for n in range(N):
    weight_list.append(int(input()))
    
weight_list = sorted(weight_list)

total_weight = []
for i, weight in enumerate(weight_list):
    total_weight.append(weight * (N - i))

biggest = max(total_weight)
print(biggest)
