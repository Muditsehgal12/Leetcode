class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = []

        for i in range(n):
            greater = -1

            for j in range(1, n):
                index = (i + j) % n

                if nums[index] > nums[i]:
                    greater = nums[index]
                    break

            ans.append(greater)

        return ans