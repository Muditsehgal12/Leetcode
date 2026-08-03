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
        def check(arr):
            stack1=[]
            r=''
            for i in range(len(arr)):
                if arr[i]=='#':
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(arr[i])
            for i in stack1:
                r+=i
            return r
        
        return check(s)==check(t)
        
                      
