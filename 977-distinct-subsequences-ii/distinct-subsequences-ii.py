class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
           
            total = sum(dp) % MOD
            dp[idx] = (total + 1) % MOD
            
        return sum(dp) % MOD