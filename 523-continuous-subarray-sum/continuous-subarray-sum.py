class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix=0
        f={0:-1}
        for i in range(len(nums)):
            prefix+=nums[i]
            r=prefix%k
            if r in f:
                if i-f[r]>1:
                    return True
            else:
                f[r]=i
        return False