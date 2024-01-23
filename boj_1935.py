import sys
import operator

n = int(input())
arr = sys.stdin.readline().rstrip()
num_list = []

for i in range(n):
    num_list.append(int(input()))

opdict = {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '%':operator.mod}


dic = {}
for j in arr:
    if j not in opdict and j not in dic:
        dic[j] = num_list.pop(0)

stack = []      
for k in arr:
    if k not in opdict:
        stack.append(dic[k])
    else:
        num2 = float(stack.pop())
        num1 = float(stack.pop())
        result = opdict[k](num1, num2)
        stack.append(result)
        
print("{:.2f}".format(stack[-1])) 
