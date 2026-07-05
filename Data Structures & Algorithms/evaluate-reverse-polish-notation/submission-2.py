class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                right_element = int(stack.pop())
                left_element = int(stack.pop())
                if token == '+':
                    answer = left_element + right_element
                elif token == '-':
                    answer = left_element - right_element
                elif token == '*':
                    answer = left_element * right_element
                elif token == '/':
                    # Python's // truncates toward negative infinity
                    # We need truncation toward zero for this problem
                    answer = int(left_element / right_element)
                stack.append(str(answer))
        return int(stack[0])
