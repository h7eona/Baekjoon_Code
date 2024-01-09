A, B = map(int, input().split())
cnt = 0

while B > A:
    if int(str(B)[-1]) == 1:
        B = int(str(B)[:-1])
        cnt += 1
    else:
        if B % 2 == 0:
            B = B // 2
            cnt += 1
        else:
            break
 
if A != 1 and B % A == 0 or A == 1 and B == 1:          
    print(cnt + 1)
else:
    print(-1)
