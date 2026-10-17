class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n /= 10 # Integer division is the default in Python 2
            return s
            
        n = len(nums)
        # Store tuples of (digit_sum, value, original_index)
        arr = []
        for i in xrange(n):
            arr.append((get_digit_sum(nums[i]), nums[i], i))
            
        # Sort based on digit sum, then by value (which matches Python's default tuple sorting)
        arr.sort()
        
        visited = [False] * n
        swaps = 0
        
        # Find cycles in the permutation to calculate minimum swaps
        for i in xrange(n):
            if visited[i] or arr[i][2] == i:
                continue
                
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1
                
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps