class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        
        min_len_at_prefix = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_so_far = float('inf')
        ans = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
               
            if current_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_len_at_prefix[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len_at_prefix[left - 1])
                min_so_far = min(min_so_far, curr_len)
                
            min_len_at_prefix[right] = min_so_far
            
        return ans if ans != float('inf') else -1