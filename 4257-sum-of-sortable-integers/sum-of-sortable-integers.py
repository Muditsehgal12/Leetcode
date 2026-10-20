class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sorted(nums)
        ans = 0
        
        # Iterate over all possible lengths of the subarray (divisors of n)
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            is_sortable = True
            
            # Check each block of size k
            for i in range(0, n, k):
                block = nums[i:i+k]
                target = s[i:i+k]
                
                drops = 0
                drop_idx = -1
                
                # Count how many times the sequence strictly decreases
                for j in range(k - 1):
                    if block[j] > block[j+1]:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            break
                
                # If there is more than 1 drop, it cannot be a rotated sorted array
                if drops > 1:
                    is_sortable = False
                    break
                
                # If 0 drops, it's already sorted; must match target exactly
                if drops == 0:
                    if block != target:
                        is_sortable = False
                        break
                # If 1 drop, rotate at the drop index and compare
                else:
                    if block[drop_idx+1:] + block[:drop_idx+1] != target:
                        is_sortable = False
                        break
                        
            if is_sortable:
                ans += k
                
        return ans