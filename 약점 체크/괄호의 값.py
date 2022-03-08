formula = list(input())

stack = []
result = 0
tmp = 1

for i in range(len(formula)):

    if formula[i] == '(':
        stack.append(formula[i])
        tmp *= 2

    elif formula[i] == '[':
        stack.append(formula[i])
        tmp *= 3
    
    elif formula[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if formula[i-1] == '(':
            result += tmp
        stack.pop()
        tmp //= 2
    
    else:
        if not stack or stack[-1] == '(':
            result =0
            break
        if formula[i-1] == '[':
            result += tmp

        stack.pop()
        tmp //= 3
    
if stack:
    print(0)
else:
    print(result)