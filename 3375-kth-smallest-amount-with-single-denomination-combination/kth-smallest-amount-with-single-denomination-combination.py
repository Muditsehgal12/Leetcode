import math

class Solution(object):
    def findKthSmallest(self, coins, k):
        """:type coins: List[int]"""
        """:type k: int"""
        """:type: int"""
        
        # Helper function to compute Greatest Common Divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Helper function to compute Least Common Multiple safely
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(coins)
        
        # Precompute LCMs for all subsets using bitmasking to avoid redundant computations
        # subsets[mask] stores the LCM of the chosen subset of coins
        subsets = [1] * (1 << n)
        for i in range(1 << n):
            for j in range(n):
                if (i >> j) & 1:
                    prev = i ^ (1 << j)
                    # If previous submask is valid, compute LCM
                    if prev == 0:
                        subsets[i] = coins[j]
                    else:
                        val = lcm(subsets[prev], coins[j])
                        # Optimization: if LCM exceeds max possible answer, cap it
                        subsets[i] = min(val, 10**12)
                    break

        # Function to count how many distinct amounts <= x can be made
        def count(x):
            total = 0
            for i in range(1 << n):
                if i == 0:
                    continue
                # Count set bits to determine the sign in Inclusion-Exclusion Principle
                set_bits = bin(i).count('1')
                lcm_val = subsets[i]
                if set_bits % 2 == 1:
                    total += x // lcm_val
                else:
                    total -= x // lcm_val
            return total

        # Binary search range
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans