num1, num2 = input().split()

new_num1 = ''.join(reversed(num1))
new_num2 = ''.join(reversed(num2))

if int(new_num1) > int(new_num2):
    print(new_num1)
else:
    print(new_num2)