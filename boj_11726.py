n = int(input())

max_num = n // 2
answer = 0

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


for i in range(max_num+1):
    other = n - 2 * i # 2x1 의 개수
    rec_list = [0] * i + [1] * other #    0은 1x2, 1은 2x1
    total = factorial(len(rec_list)) // (factorial(i) * factorial(other))
    answer += total

print(answer%10007)
