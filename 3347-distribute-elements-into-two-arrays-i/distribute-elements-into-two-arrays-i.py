class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[nums[0]]
        arr2=[nums[1]]
        i=2
        while i<len(nums):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
                i+=1
            else:
                arr2.append(nums[i])
                i+=1
        a=arr1+arr2
        return a