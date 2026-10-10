class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # If we have enough operations to make all elements equal
        if sum(diffs) <= k:
            return 0
            
        # Max difference according to constraints is 10^5
        cnt = [0] * 100001
        for d in diffs:
            cnt[d] += 1
            
        # Greedily reduce the maximum differences
        for i in xrange(100000, 0, -1):
            if cnt[i] > 0:
                if k >= cnt[i]:
                    # We have enough operations to reduce all elements of difference `i` to `i-1`
                    cnt[i - 1] += cnt[i]
                    k -= cnt[i]
                    cnt[i] = 0
                else:
                    # We can only reduce `k` elements of difference `i` to `i-1`
                    cnt[i - 1] += k
                    cnt[i] -= k
                    break
                    
        # Calculate the final sum of squared differences
        ans = 0
        for i in xrange(1, 100001):
            if cnt[i] > 0:
                ans += cnt[i] * (i ** 2)
                
        return ans