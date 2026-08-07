class Solution:
    def smallestNumber(self, num, t):
        temp_t = t
        counts = [0, 0, 0, 0]
        for idx, p in enumerate([2, 3, 5, 7]):
            while temp_t % p == 0:
                counts[idx] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"
            
        c2, c3, c5, c7 = counts

        def get_factors(d):
            f2 = f3 = f5 = f7 = 0
            while d % 2 == 0:
                f2 += 1
                d //= 2
            while d % 3 == 0:
                f3 += 1
                d //= 3
            if d == 5:
                f5 += 1
            if d == 7:
                f7 += 1
            return f2, f3, f5, f7

        def min_digits_needed(r2, r3, r5, r7):
            r2 = max(0, r2)
            r3 = max(0, r3)
            r5 = max(0, r5)
            r7 = max(0, r7)
            
            n9 = r3 // 2
            rem3 = r3 % 2
            n8 = r2 // 3
            rem2 = r2 % 3
            
            n6 = 0
            if rem2 == 1 and rem3 == 1:
                n6 = 1
                rem2 = 0
                rem3 = 0
            elif rem2 == 2 and rem3 == 1:
                n6 = 1
                rem2 = 1
                rem3 = 0
                
            n7 = r7
            n5 = r5
            n4 = rem2 // 2
            n3 = rem3
            n2 = rem2 % 2
            
            return n9 + n8 + n7 + n6 + n5 + n4 + n3 + n2

        def build_smallest_suffix(rem_len, r2, r3, r5, r7):
            suffix = []
            cur_r2, cur_r3, cur_r5, cur_r7 = max(0, r2), max(0, r3), max(0, r5), max(0, r7)
            
            for pos in range(rem_len):
                remaining_slots = rem_len - 1 - pos
                for d in range(1, 10):
                    f2, f3, f5, f7 = get_factors(d)
                    next_r2 = cur_r2 - f2
                    next_r3 = cur_r3 - f3
                    next_r5 = cur_r5 - f5
                    next_r7 = cur_r7 - f7
                    
                    if min_digits_needed(next_r2, next_r3, next_r5, next_r7) <= remaining_slots:
                        suffix.append(str(d))
                        cur_r2, cur_r3, cur_r5, cur_r7 = next_r2, next_r3, next_r5, next_r7
                        break
            return "".join(suffix)

        n = len(num)
        first_zero = num.find('0')
        max_prefix_len = first_zero if first_zero != -1 else n

        pref_2, pref_3, pref_5, pref_7 = 0, 0, 0, 0
        prefix_factors = [(0, 0, 0, 0)]
        for i in range(max_prefix_len):
            d = int(num[i])
            f2, f3, f5, f7 = get_factors(d)
            pref_2 += f2
            pref_3 += f3
            pref_5 += f5
            pref_7 += f7
            prefix_factors.append((pref_2, pref_3, pref_5, pref_7))

        if first_zero == -1:
            if pref_2 >= c2 and pref_3 >= c3 and pref_5 >= c5 and pref_7 >= c7:
                return num

        for i in range(max_prefix_len, -1, -1):
            p2, p3, p5, p7 = prefix_factors[i]
            rem_len = n - i
            
            if rem_len == 0:
                continue

            start_digit = int(num[i]) + 1 if i < n else 1
            
            for d in range(start_digit, 10):
                f2, f3, f5, f7 = get_factors(d)
                req2 = c2 - p2 - f2
                req3 = c3 - p3 - f3
                req5 = c5 - p5 - f5
                req7 = c7 - p7 - f7
                
                if min_digits_needed(req2, req3, req5, req7) <= rem_len - 1:
                    suffix = build_smallest_suffix(rem_len - 1, req2, req3, req5, req7)
                    return num[:i] + str(d) + suffix

        min_needed = min_digits_needed(c2, c3, c5, c7)
        target_len = max(n + 1, min_needed)
        
        return build_smallest_suffix(target_len, c2, c3, c5, c7)