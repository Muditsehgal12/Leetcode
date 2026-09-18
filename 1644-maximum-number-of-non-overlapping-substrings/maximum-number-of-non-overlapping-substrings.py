class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        
        for i in xrange(n):
            c = ord(s[i]) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i
            
        v = []
        for c in xrange(26):
            if last[c] == -1:
                continue
            l = first[c]
            r = last[c]
            ok = True
            
            i = l
            while i <= r:
                d = ord(s[i]) - ord('a')
                if first[d] < l:
                    ok = False
                    break
                r = max(r, last[d])
                i += 1
                
            if ok:
                v.append((r, l))
                
        v.sort()
        ans = []
        prev_r = -1
        
        for nr, l in v:
            if l > prev_r:
                ans.append(s[l:nr + 1])
                prev_r = nr
                
        return ans