class Solution(object):
    def maximumWeight(self, intervals):
        arr = []

        for i in range(len(intervals)):
            l, r, w = intervals[i]
            arr.append([l, r, w, i])

        arr.sort()

        n = len(arr)

        nxt = [n] * n

        for i in range(n):
            lo = i + 1
            hi = n - 1
            ans = n

            while lo <= hi:
                mid = (lo + hi) // 2

                if arr[mid][0] > arr[i][1]:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            nxt[i] = ans

        memo = {}

        def dp(i, k):

            if i == n or k == 0:
                return (0, [])

            if (i, k) in memo:
                return memo[(i, k)]

            skip = dp(i + 1, k)

            wt, ids = dp(nxt[i], k - 1)

            take = (
                wt + arr[i][2],
                sorted(ids + [arr[i][3]])
            )

            if take[0] > skip[0]:
                ans = take
            elif take[0] < skip[0]:
                ans = skip
            else:
                if take[1] < skip[1]:
                    ans = take
                else:
                    ans = skip

            memo[(i, k)] = ans
            return ans

        return dp(0, 4)[1]