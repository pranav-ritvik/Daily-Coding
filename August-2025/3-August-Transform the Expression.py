# cook your dish here
t = int(input())
precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

for test_case in range(t):
    expr = input().strip()
    stack = []
    output = []
    for char in expr:
        if char.isalpha():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif char in precedence:
            while (stack and stack[-1] != '(' and
                   ((precedence[char] < precedence[stack[-1]]) or
                    (precedence[char] == precedence[stack[-1]] and char != '^'))):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    print("".join(output))
