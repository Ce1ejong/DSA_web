# Stack Implementation (python_scripts/stack.py)
# Operations: Stacks, Infix to Postfix/Prefix, Evaluation

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

# Utility for expression conversion and evaluation
def precedence(operator):
    """Defines the precedence of operators."""
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    """Converts an infix expression to a postfix expression."""
    output = []
    stack = Stack()
    for char in expression:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9':
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop() # Pop the '('
        else: # Operator
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(char)):
                output.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        output.append(stack.pop())
    return " ".join(output)

def evaluate_postfix(expression):
    """Evaluates a postfix expression."""
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else: # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+': stack.push(operand1 + operand2)
            elif token == '-': stack.push(operand1 - operand2)
            elif token == '*': stack.push(operand1 * operand2)
            elif token == '/': stack.push(operand1 / operand2)
    return stack.pop()

# Example Usage:
if __name__ == "__main__":
    infix = "A+B*C"
    postfix_result = infix_to_postfix(infix)
    print(f"Infix: {infix}, Postfix: {postfix_result}") # Output: A B C * +
    
    # Evaluation example: 2 * 3 + 5 = 11
    eval_expression = "2 3 * 5 +"
    eval_result = evaluate_postfix(eval_expression)
    print(f"Evaluation of {eval_expression}: {eval_result}") # Output: 11