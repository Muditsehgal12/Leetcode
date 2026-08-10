class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        last={}
        seen=set()
        for i in range(len(s)):
            last[s[i]]=i
        
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and s[i]<stack[-1] and last[stack[-1]]>i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return ''.join(stack)
