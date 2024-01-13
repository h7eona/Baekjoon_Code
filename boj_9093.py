import sys
T = int(input())

sentense_list = []
for _ in range(T):
    sentense_list.append(list(map(str, input().split())))

for sen in sentense_list:
    for word in sen:
        print(word[::-1], end=' ')    
