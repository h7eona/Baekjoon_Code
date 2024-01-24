while True:
    try:
        sen = list(input())
        ans = [0] * 4
        for w in sen:
            if 48<=ord(w)<=57:
                ans[2] += 1
            elif ord(w) == 32:
                ans[3] += 1
            elif 65<=ord(w)<=90:
                ans[1] += 1
            elif 97<=ord(w)<=122:
                ans[0] += 1
        print(*ans)
    except EOFError:
        break
