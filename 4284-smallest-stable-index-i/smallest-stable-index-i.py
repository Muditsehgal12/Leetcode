class Solution(object):
    def firstStableIndex(self, nums, k):
        a,b,c=0,0,0
        for i in range(len(nums)):
            a = max(nums[0:i+1])
            b = min(nums[i:len(nums)])
            c = a - b

            if c <= k:
                return i

        return -1