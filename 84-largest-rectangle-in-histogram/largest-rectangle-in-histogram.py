class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        n=len(heights)
        left=[-1]*n
        right=[n]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                left[i]=-1
            else:
                left[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                right[i]=n
            else:
                right[i]=stack[-1]
            stack.append(i)
        maxi=0
        for i in range(n):
            w=right[i]-left[i]-1
            area=w*heights[i]
            maxi=max(maxi,area)
        return maxi
        

