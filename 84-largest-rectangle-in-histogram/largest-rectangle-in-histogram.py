class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        stack=[]
        left=[-1]*n
        right=[n]*n
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                left[i]=-1
            else:
                left[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                right[i]=n
            else:
                right[i]=stack[-1]
            stack.append(i)
        Marea=0
        for i in range(n):
            w=right[i]-left[i]-1
            area=w*heights[i]
            Marea=max(Marea,area)
        return Marea
        