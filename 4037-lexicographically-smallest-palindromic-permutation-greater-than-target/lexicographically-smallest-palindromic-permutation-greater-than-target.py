from collections import Counter

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        count = Counter(s)
        
        odd_chars = [ch for ch, freq in count.items() if freq % 2 != 0]
        if n % 2 == 0 and len(odd_chars) > 0:
            return ""
        if n % 2 != 0 and len(odd_chars) != 1:
            return ""
            
        mid_char = odd_chars[0] if n % 2 != 0 else ""
        if mid_char:
            count[mid_char] -= 1
            
        half_len = n // 2
        
        # Get sorted list of available characters for the first half
        keys = sorted(count.keys())
        counts = [count[k] // 2 for k in keys]
        
        def backtrack(idx, current_half):
            if idx == half_len:
                candidate = "".join(current_half)
                full_palindrome = candidate + mid_char + candidate[::-1]
                return full_palindrome if full_palindrome > target else ""
            
            # Try to place characters greedily
            for i in range(len(keys)):
                if counts[i] > 0:
                    # Pruning: check if we can form a valid suffix
                    counts[i] -= 1
                    current_half.append(keys[i])
                    
                    # Quick prefix check against target
                    candidate = "".join(current_half)
                    target_prefix = target[:len(candidate)]
                    
                    # Only proceed down this path if it's still possible to match or exceed target
                    valid = True
                    if candidate < target_prefix:
                        valid = False
                    elif candidate == target_prefix:
                        # Check if remaining character pool can form something >= remaining target
                        rem_target = target[len(candidate):half_len]
                        # Construct lexicographically largest possible completion
                        largest_rem = []
                        for j in range(len(keys)):
                            largest_rem.extend([keys[j]] * counts[j])
                        # sort descending for max
                        largest_rem.sort(reverse=True)
                        if "".join(largest_rem) < rem_target:
                            valid = False
                    
                    if valid:
                        res = backtrack(idx + 1, current_half)
                        if res:
                            return res
                    
                    current_half.pop()
                    counts[i] += 1
                    
            return ""

        return backtrack(0, [])