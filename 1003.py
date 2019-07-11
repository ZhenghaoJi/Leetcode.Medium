class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for s in S:
            stack.append(s)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0
# no use remove()
