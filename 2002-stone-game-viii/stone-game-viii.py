class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        # Compute prefix sums
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stones[i]
            
        
        res = pref[n - 1]
        for i in range(n - 2, 0, -1):
            res = max(res, pref[i] - res)
            
        return res