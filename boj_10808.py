word = list(input())
ans = [0] * 26

for i in word:
    idx = ord(i) - ord('a')
    ans[idx] += 1

print(*ans)
