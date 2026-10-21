class Solution(object):

  def minOperations(self, s):
    """:type s: str

    :rtype: int
    """
    n = len(s)

    # 1. Already sorted
    if all(s[i] <= s[i + 1] for i in range(n - 1)):
      return 0

    # 2. Cannot sort length 2 string using proper substrings
    if n == 2:
      return -1

    mn = min(s)
    mx = max(s)

    # 3. Can be sorted in 1 operation
    if s[0] == mn or s[-1] == mx:
      return 1

    # 4. Requires 3 operations if min is ONLY at index n-1 AND max is ONLY at index 0
    if s.find(mn) == n - 1 and s.rfind(mx) == 0:
      return 3

    # 5. All other cases require 2 operations
    return 2