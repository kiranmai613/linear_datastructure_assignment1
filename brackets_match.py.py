def check_brackets(code):
    stack = []
    opening = "([{"
    closing = ")]}"
    
    for char in code:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            elif opening.index(stack[-1]) == closing.index(char):
                stack.pop()
            else:
                return False
                
    return not stack

code = "(3+2)"
print(check_brackets(code))




