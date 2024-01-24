word = list(input())
ans = []
for i in range(len(word)):
    new = word[i:]
    ans.append(new)
    
answer = sorted(ans)
for w in answer:
    print(*w, sep='')
