class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        invalid=set()
        ans=''
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif not stack and s[i]==')':
                invalid.add(i)
            elif stack and s[i]==')':
                stack.pop()
        if stack:
            for i in stack:
                invalid.add(i)
        for i in range(len(s)):
            if i not in invalid:
                ans+=s[i]
        return ans
        
            
