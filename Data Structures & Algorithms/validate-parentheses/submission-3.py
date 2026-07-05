class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in brackets:
                stack.append(i)
            elif i in brackets.values():
                if not stack or brackets[stack[-1]] != i:
                    return False
                else:
                    stack.pop()  
        return len(stack) == 0