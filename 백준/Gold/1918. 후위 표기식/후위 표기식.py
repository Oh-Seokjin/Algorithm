import sys

operator = sys.stdin.readline().rstrip()
stack = []
answer = ""

for token in operator:
    if 'A' <= token <= 'Z': # 피연산자면 바로 추가
        answer += token
    elif token == '(': # 닫는 괄호 나오기 전까지 쌓아둠
        stack.append('(')
    elif token == '*' or token == '/': 
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(token)
    elif token == '+' or token == '-':
        while stack and (stack[-1] !='('):
            answer += stack.pop()
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

while stack:
    answer += stack.pop()

print(answer)