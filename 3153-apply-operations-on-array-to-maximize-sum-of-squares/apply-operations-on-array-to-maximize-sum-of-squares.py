class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        # Count the number of set bits at each position across all numbers
        for num in nums:
            for i in xrange(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        max_sum = 0
        
        # Greedily construct the k largest numbers
        for _ in xrange(k):
            current_num = 0
            for i in xrange(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Add the square of the constructed number to the total sum
            max_sum = (max_sum + current_num * current_num) % MOD
            
        return max_sum