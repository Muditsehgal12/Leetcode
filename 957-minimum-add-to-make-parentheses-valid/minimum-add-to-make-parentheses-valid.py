class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)