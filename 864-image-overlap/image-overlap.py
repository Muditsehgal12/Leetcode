class Solution(object):
    def largestOverlap(self, img1, img2):

        A = []
        B = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    A.append((i, j))
                if img2[i][j]:
                    B.append((i, j))

        d = {}
        ans = 0

        for x1, y1 in A:
            for x2, y2 in B:
                shift = (x1 - x2, y1 - y2)

                if shift not in d:
                    d[shift] = 1
                else:
                    d[shift] += 1

                ans = max(ans, d[shift])

        return ans