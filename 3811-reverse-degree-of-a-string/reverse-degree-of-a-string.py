class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            m=ord(s[i])-ord('a')+1
            a=(i+1)*(27-m)
            ans+=a
            a=0
            m=0
        return ans