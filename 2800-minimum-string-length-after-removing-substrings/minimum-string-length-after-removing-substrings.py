class Solution(object):
    def minLength(self, s):
        stack = []
        i = 0

        while i < len(s):
            if stack and s[i] == "B" and stack[-1] == "A":
                stack.pop()
            elif stack and s[i] == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(s[i])
            i += 1

        return len(stack)