class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        cnt0 = 0

        for x in nums:
            xor ^= x
            if x == 0:
                cnt0 += 1

        n = len(nums)

        if xor != 0:
            return n

        if cnt0 == n:
            return 0

        return n - 1