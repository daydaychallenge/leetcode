
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        #### [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

        Given a string **S** and a string **T**, count the number of distinct subsequences of **S** which equals **T**.

        A subsequence of a string is a new string which is formed from the  original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not).

        It's guaranteed the answer fits on a 32-bit signed integer.

        **Example 1:**

        ```
        Input: S = "rabbbit", T = "rabbit"
        Output: 3
        Explanation:
        As shown below, there are 3 ways you can generate "rabbit" from S.
        (The caret symbol ^ means the chosen letters)

        rabbbit
        ^^^^ ^^
        rabbbit
        ^^ ^^^^
        rabbbit
        ^^^ ^^^
        ```

        **Example 2:**

        ```
        Input: S = "babgbag", T = "bag"
        Output: 5
        Explanation:
        As shown below, there are 5 ways you can generate "bag" from S.
        (The caret symbol ^ means the chosen letters)

        babgbag
        ^^ ^
        babgbag
        ^^    ^
        babgbag
        ^    ^^
        babgbag
          ^  ^^
        babgbag
            ^^^
        ```

        Parameters
        ----------
        s: str
        t: str

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/4294105.html

        """
        lens, lent = len(s), len(t)
        dp = [[0 for _ in range(lens+1)] for _ in range(lent+1)]
        for j in range(lens+1):
            dp[0][j] = 1

        for i in range(1, lent+1):
            for j in range(1, lens+1):
                dp[i][j] = dp[i-1][j-1]+dp[i][j-1] if s[j-1] == t[i-1] else dp[i][j-1]

        return dp[-1][-1]
