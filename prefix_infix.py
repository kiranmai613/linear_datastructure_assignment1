# Q6. Write a program to convert prefix expression to infix expression
def prefix_to_infix(prefix):
    stack = []
    # Reverse the prefix expression to process it from right to left
    prefix = prefix[::-1]
    
    for token in prefix:
        if token.isalpha() or token.isdigit():
            # If the token is an operand, push it to the stack
            stack.append(token)
        else:
            # If the token is an operator, pop the top two operands from the stack and combine them with the operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = f"({operand1}{token}{operand2})"
            stack.append(expression)
    
    # The final expression in the stack is the infix expression
    return stack[-1]

prefix = "*+AB-CD"
infix = prefix_to_infix(prefix)
print(infix) 
