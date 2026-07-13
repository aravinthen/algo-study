class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        par_map = {"(": ")", "{": "}", "[":"]"}

        stack = []

        for i in s:
            if i in par_map:
                stack.append(i)
            else:
                if not stack or i != par_map[stack[-1]]:
                    return False
                stack.pop()

        return len(stack) == 0 
        