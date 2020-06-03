
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        #### [91. Decode Ways](https://leetcode.com/problems/decode-ways/)

        A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

        ```
        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        ```

        Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

        **Example 1:**

        ```
        Input: "12"
        Output: 2
        Explanation: It could be decoded as "AB" (1 2) or "L" (12).
        ```

        **Example 2:**

        ```
        Input: "226"
        Output: 3
        Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
        ```

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        if not s or s[0] == '0': return 0
        if len(s) == 1: return 1
        dp0 = dp1 = 1
        for i in range(1, len(s)+1):
            dpi = 0
            dpi += dp1 if s[i-1] != '0' else 0
            if i >= 2 and (s[i-2] == '1' or 20 <= int(s[i-2:i]) <= 26):
                dpi += dp0
            dp0, dp1 = dp1, dpi
        return dp1
