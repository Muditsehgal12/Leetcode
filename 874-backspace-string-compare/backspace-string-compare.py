class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        m=''
        r=''
        for i in range(len(s)):
            if s[i]=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])
        for i in stack1:
            r+=i
        
        for i in range(len(t)):
            if t[i]=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[i])
        for i in stack2:
            m+=i
        return r==m
        
                      
