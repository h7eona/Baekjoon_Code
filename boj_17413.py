import sys

S = list(sys.stdin.readline().rstrip())

stack = []
tmp_stack = []
ans = []
flag = 1
for alpha in S:
    if alpha == '<':
        flag = 0
        if len(stack) > 0:
            tmp = stack[::-1]
            tmp = ''.join(tmp)
            ans.append(tmp)
            stack = []
    elif alpha == '>':
        flag = 1
        if len(tmp_stack) > 0:
            tmp = ''.join(tmp_stack)
            tmp = '<' + tmp + '>'
            ans.append(tmp)
            tmp_stack = []
    else:
        if flag == 0:
            tmp_stack.append(alpha)
        else:
            if alpha == ' ':
                rev_word = stack[::-1]
                rev_word = ''.join(rev_word)
                ans.append(rev_word)
                ans.append(alpha)
                stack = []
            else:
                stack.append(alpha)

if len(stack) > 0:
    tmp = stack[::-1]
    tmp = ''.join(tmp)
    ans.append(tmp)
    stack = []

print(''.join(ans))
