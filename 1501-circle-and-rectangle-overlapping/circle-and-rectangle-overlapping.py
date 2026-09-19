class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        cx=max(x1,min(x2,xCenter))
        cy=max(y1,min(y2,yCenter))
        a=(cx-xCenter)**2+(cy-yCenter)**2
        if a<=radius**2:
            return True
        return False