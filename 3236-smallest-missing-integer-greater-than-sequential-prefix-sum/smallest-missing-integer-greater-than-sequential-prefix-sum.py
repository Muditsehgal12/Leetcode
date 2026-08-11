class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]+1
        
        s=0
        stack=[]
        stack.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]-stack[-1]==1:
                stack.append(nums[i])
            else:
                break
        for i in stack:
            s+=i
        while s in nums:
            s+=1
        return s
