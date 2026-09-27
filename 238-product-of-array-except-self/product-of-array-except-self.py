class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= prefix
            prefix *= nums[i]

        return ans