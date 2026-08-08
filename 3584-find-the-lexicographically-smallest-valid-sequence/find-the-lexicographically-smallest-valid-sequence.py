class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)

        suf = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        ans = []
        i = j = 0
        used = False

        while i < n and j < m:
            if word1[i] == word2[j]:
                ans.append(i)
                i += 1
                j += 1

            elif not used:
                
                if j == m - 1 or (j + 1 < m and suf[j + 1] > i):
                    ans.append(i)
                    used = True
                    i += 1
                    j += 1
                else:
                    i += 1
            else:
                i += 1

        return ans if len(ans) == m else []