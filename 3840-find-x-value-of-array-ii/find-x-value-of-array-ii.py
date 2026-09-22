class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        n2 = 1
        while n2 < n:
            n2 <<= 1
            
        # tree_prod[i] stores the product modulo k for node i
        tree_prod = [1] * (2 * n2)
        # tree_freq[i] stores the frequency array of size k for node i
        tree_freq = [[0] * k for _ in range(2 * n2)]
        
        def merge(left_idx, right_idx, parent_idx):
            lp = tree_prod[left_idx]
            rp = tree_prod[right_idx]
            tree_prod[parent_idx] = (lp * rp) % k
            
            lf = tree_freq[left_idx]
            rf = tree_freq[right_idx]
            pf = tree_freq[parent_idx]
            
            for i in range(k):
                pf[i] = lf[i]
                
            for i in range(k):
                if rf[i] > 0:
                    r = (lp * i) % k
                    pf[r] += rf[i]

        # Initialize leaves
        for i in range(n):
            v = nums[i] % k
            idx = n2 + i
            tree_prod[idx] = v
            tree_freq[idx][v] = 1
            
        # Build tree bottom-up
        for i in range(n2 - 1, 0, -1):
            merge(i << 1, (i << 1) + 1, i)
            
        def update(idx, x):
            idx += n2
            tree_prod[idx] = x
            for i in range(k):
                tree_freq[idx][i] = 0
            tree_freq[idx][x] = 1
            
            idx >>= 1
            while idx >= 1:
                merge(idx << 1, (idx << 1) + 1, idx)
                idx >>= 1

        # Reusable temporary state for query combination
        def query(l, r):
            # L and R accumulators
            l_prod = 1
            l_freq = [0] * k
            r_prod = 1
            r_freq = [0] * k
            
            l += n2
            r += n2
            
            while l <= r:
                if l & 1:
                    # Merge l_acc with tree[l]
                    np = (l_prod * tree_prod[l]) % k
                    nf = [0] * k
                    for i in range(k):
                        nf[i] = l_freq[i]
                    tf = tree_freq[l]
                    for i in range(k):
                        if tf[i] > 0:
                            r_idx = (l_prod * i) % k
                            nf[r_idx] += tf[i]
                    l_prod = np
                    l_freq = nf
                    l += 1
                    
                if not (r & 1):
                    # Merge tree[r] with r_acc
                    np = (tree_prod[r] * r_prod) % k
                    nf = [0] * k
                    tf = tree_freq[r]
                    for i in range(k):
                        nf[i] = tf[i]
                    for i in range(k):
                        if r_freq[i] > 0:
                            r_idx = (tree_prod[r] * i) % k
                            nf[r_idx] += r_freq[i]
                    r_prod = np
                    r_freq = nf
                    r -= 1
                    
                l >>= 1
                r >>= 1
                
            # Combine l_freq and r_freq
            res_freq = [0] * k
            for i in range(k):
                res_freq[i] = l_freq[i]
            for i in range(k):
                if r_freq[i] > 0:
                    r_idx = (l_prod * i) % k
                    res_freq[r_idx] += r_freq[i]
            return res_freq

        ans = []
        for idx, val, start, x in queries:
            v = val % k
            update(idx, v)
            res_freq = query(start, n - 1)
            ans.append(res_freq[x])
            
        return ans