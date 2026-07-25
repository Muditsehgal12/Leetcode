class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        st = []
        
        a=[-1]*n
        for i in range(2*n):
            while st and nums[st[-1]]<nums[i%n]:
                a[st.pop()]=nums[i%n]
            st.append(i%n)
        
        return a