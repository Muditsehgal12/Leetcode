class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=len(nums)-1
        p=len(nums)-1
        a=[0]*len(nums)
        while i<=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                a[p]=nums[i]*nums[i]
                i+=1
                p-=1
            else:
                a[p]=nums[j]*nums[j]
                j-=1
                p-=1
        return a