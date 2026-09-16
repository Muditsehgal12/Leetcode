class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # We need to calculate C(n + k - 1, 2k)
        N = n + k - 1
        K = 2 * k
        
        # Combinations can get large, but Python handles arbitrarily large integers.
        # C(N, K) = N! / (K! * (N - K)!)
        if K < 0 or K > N:
            return 0
        if K == 0 or K == N:
            return 1
            
        if K > N // 2:
            K = N - K
            
        res = 1
        for i in range(1, K + 1):
            res = res * (N - i + 1) // i
            
        return res % MOD