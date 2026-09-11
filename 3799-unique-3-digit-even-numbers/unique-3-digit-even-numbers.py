class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        from collections import Counter
        
        # Count available frequencies of each digit from the input
        available = Counter(digits)
        count = 0
        
        # Iterate through all possible 3-digit even numbers (100 to 998, step by 2)
        for num in range(100, 1000, 2):
            s = str(num)
            needed = Counter(s)
            
            # Check if we have enough of each digit to form this number
            possible = True
            for digit_char, freq in needed.items():
                digit_val = int(digit_char)
                if available[digit_val] < freq:
                    possible = False
                    break
            
            if possible:
                count += 1
                
        return count