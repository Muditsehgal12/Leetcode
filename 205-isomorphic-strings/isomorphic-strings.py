class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        f={}
        for i in range(len(s)):
            if s[i] in f:
                if f[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in f.values():
                    return False
                f[s[i]]=t[i]
        res=""
        for i in s:
            res+=f[i]
        if res==t:
            return True
        return False