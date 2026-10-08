class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=0
        stack=[]
        for i in s:
            if i=='(':
                if d>0:
                    stack.append(i)
                d+=1
            else:
                if d>1:
                    stack.append(i)
                d-=1
        return "".join(stack)