class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        r=0
        freq={}
        i=0
        freq[s[i]]=1
        for j in range(1,len(s)):
            freq[s[j]]=freq.get(s[j],0)+1
            while freq[s[j]]>2 and j>=i:
                freq[s[i]]-=1
                i+=1
            m=j-i+1
            r=max(r,m)
            
        return r                