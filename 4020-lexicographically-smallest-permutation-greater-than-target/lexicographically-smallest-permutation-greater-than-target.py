class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(target)

        for pos in xrange(n - 1, -1, -1):

            remain = freq[:]
            possible = True

            for i in xrange(pos):
                idx = ord(target[i]) - ord('a')

                if remain[idx] == 0:
                    possible = False
                    break

                remain[idx] -= 1

            if not possible:
                continue

            cur = ord(target[pos]) - ord('a')

            for nxt in xrange(cur + 1, 26):

                if remain[nxt] == 0:
                    continue

                remain[nxt] -= 1

                ans = target[:pos] + chr(ord('a') + nxt)

                for c in xrange(26):
                    ans += chr(ord('a') + c) * remain[c]

                return ans

        return ""