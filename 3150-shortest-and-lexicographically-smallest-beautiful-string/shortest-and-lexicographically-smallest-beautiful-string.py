class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ans = ""
        n = len(s)

        for i in xrange(n):
            ones = 0

            for j in xrange(i, n):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    cur = s[i:j + 1]

                    if (ans == "" or
                        len(cur) < len(ans) or
                        (len(cur) == len(ans) and cur < ans)):
                        ans = cur

                elif ones > k:
                    break

        return ans