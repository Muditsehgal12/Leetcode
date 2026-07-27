class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr=[]
        i=0
        ans=[]
        def subset(i,curr):
            if i==len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[i])
            subset(i+1,curr)

            curr.pop()
            subset(i+1,curr)
        subset(i,curr)
        return ans