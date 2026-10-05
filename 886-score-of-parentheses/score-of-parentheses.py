class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append(c)
                c=0
                
            else:
                p=stack.pop()
                c=p+max(2*c,1)
                
            
        return c        