class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        sign=+1
        result=0
        stack=[]
        num=''
        while i<len(s):
            if s[i].isdigit():
                num=''
                while i<len(s) and s[i].isdigit():
                    num=num+s[i]
                    i+=1
                result=result+sign*int(num)
                
            elif s[i]=='-':
                sign=-1
                i+=1
            elif s[i]=='+':
                sign=+1
                i+=1
            elif s[i]=='(':
                a=(result,sign)
                stack.append(a)
                result=0
                sign=+1
                i+=1
            elif s[i]==')':
                u=stack.pop()
                m=u[0]
                n=u[1]
                result=result*n+m
                i+=1
            else:
                i+=1
                continue
        return result
                
