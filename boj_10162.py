T = int(input())
ans = []

if T % 10 != 0:
    print(-1)
else:
    
    for min in [5 * 60, 1 * 60, 10]:
        num = T // min
        ans.append(str(num))
        T = T % min
    
    print(' '.join(ans))
