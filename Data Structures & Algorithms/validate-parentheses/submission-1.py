class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in brackets:
                stack.append(i)
            elif i in brackets.values():
                if not stack or brackets[stack.pop()] != i:
                    return False
            
        return len(stack) == 0

        