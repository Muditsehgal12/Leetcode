class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        f={}
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                f[stack[-1]]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
        ans=[]
        for i in nums1:
            ans.append(f.get(i,-1))
        return ans

