class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        stack=[]
        while i<len(s):
            if stack and s[i]=="B" and stack[-1]=="A":
                stack.pop()
                i+=1
            elif stack and s[i]=="D" and stack[-1]=="C":
                stack.pop()
                i+=1
            else:
                stack.append(s[i])
                i+=1
        return len(stack)
