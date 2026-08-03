class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        r=''    
        p=''
        for i in range(len(s)):
            if stack and s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
                
        for i in stack:
            p=p+i
        return p