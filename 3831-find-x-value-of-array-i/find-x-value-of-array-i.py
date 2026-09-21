class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            m = num % k
            new_dp = [0] * k

            # Start a new subarray with current element
            new_dp[m] += 1

            # Extend previous subarrays
            for r in xrange(k):
                if dp[r]:
                    new_rem = (r * m) % k
                    new_dp[new_rem] += dp[r]

            # Add counts to final answer
            for r in xrange(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans