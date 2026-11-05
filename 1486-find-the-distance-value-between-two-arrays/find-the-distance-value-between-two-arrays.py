import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        
        for x in arr1:
            # Find the insertion point for x in sorted arr2
            idx = bisect.bisect_left(arr2, x)
            
            # Check the element just greater than or equal to x
            valid = True
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
            # Check the element just smaller than x
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                count += 1
                
        return count