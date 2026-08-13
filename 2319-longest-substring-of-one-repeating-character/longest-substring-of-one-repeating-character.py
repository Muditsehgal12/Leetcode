class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        s = list(s)

        tree = [None] * (4 * n)

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left

            length = left[0] + right[0]

            pref_char = left[1]
            pref_len = left[2]

            if left[2] == left[0] and left[4] == right[1]:
                pref_len = left[0] + right[2]

            suff_char = right[4]
            suff_len = right[5]

            if right[5] == right[0] and left[4] == right[1]:
                suff_len = right[0] + left[5]

            best = max(left[3], right[3])

            if left[4] == right[1]:
                best = max(best, left[5] + right[2])

            return (
                length,
                pref_char,
                pref_len,
                best,
                suff_char,
                suff_len
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (1, s[l], 1, 1, s[l], 1)
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (1, ch, 1, 1, ch, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            s[idx] = ch
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][3])

        return ans