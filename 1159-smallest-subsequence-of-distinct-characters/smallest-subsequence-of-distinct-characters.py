class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        list={}
        seen=set()
        for i in range(len(s)):
            list[s[i]]=i
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and s[i]<stack[-1] and list[stack[-1]]>i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return ''.join(stack)
