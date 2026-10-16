class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays
        sum_sq = [0] * (4 * n)
        sum_c = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, l, r, val):
            # (c + val)^2 = c^2 + 2*c*val + val^2
            length = r - l + 1
            sum_sq[node] = (sum_sq[node] + 2 * val * sum_c[node] + val * val * length) % MOD
            sum_c[node] = (sum_c[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
            
        def pushdown(node, l, r):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0
                
        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            
            pushdown(node, l, r)
            mid = (l + r) // 2
            
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
            sum_c[node] = (sum_c[2 * node] + sum_c[2 * node + 1]) % MOD

        last = {}
        ans = 0
        
        for i, x in enumerate(nums):
            # Find the last occurrence of the current number (or -1 if it hasn't appeared)
            prev = last.get(x, -1)
            
            # Increment the distinct counts for all subarrays starting between prev + 1 and i
            update(1, 0, n - 1, prev + 1, i, 1)
            
            # Add the sum of squares of all subarrays ending at current index `i`
            ans = (ans + sum_sq[1]) % MOD
            
            # Update the last seen position of the current element
            last[x] = i
            
        return ans