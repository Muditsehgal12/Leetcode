class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=''
        stack=[]
        for i in range(len(s)):
            
            if stack and s[i].lower()==stack[-1].lower() and s[i]!=stack[-1]:
                stack.pop()             
            else:
                stack.append(s[i])
        for i in stack:
            r+=i
        return r