s = '[[{{(({[()[][][][][[]]]}))}}]]'

def isValid(s):
    if len(s) % 2 != 0: return False
    stack = []
    opens = set('{[(')
    for ch in s:
        if ch in opens:
            stack.append(ch)
        elif ch == ']' and stack[-1] == '[':
            stack.pop()
        elif ch == '}' and stack[-1] == '{':
            stack.pop()
        elif ch == ')' and stack[-1] == '(':
            stack.pop()
        else:
            return False
    return len(stack) == 0
    
print(isValid(s))