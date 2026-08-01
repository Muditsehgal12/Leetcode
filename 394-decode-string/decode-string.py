class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        n=0
        r=""
        for i in range(len(s)):
            if s[i].isdigit():
                n=n*10+int(s[i])
            elif s[i].isalpha():
                r=r+s[i]
            elif s[i]=="[":
                
                stack.append((r,n))
                n=0
                r=""
            else:
                u=stack.pop()
                w=u[0]
                z=u[1]
                r=w+z*r
                n=0
                
        
        return r