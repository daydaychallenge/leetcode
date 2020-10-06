

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        ### [1216. Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/)

        Given a string `s` and an integer `k`, find out if the given string is a *K-Palindrome* or not.

        A string is K-Palindrome if it can be transformed into a palindrome by removing at most `k` characters from it.



        **Example 1:**

        ```
        Input: s = "abcdeca", k = 2
        Output: true
        Explanation: Remove 'b' and 'e' characters.
        ```

        **Constraints:**

        - `1 <= s.length <= 1000`
        - `s` has only lowercase English letters.
        - `1 <= k <= s.length`


        Parameters
        ----------
        s: str
        k: int

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.isValidPalindrome('abcdeca', 2)

        Notes
        -----

        References
        ---------

        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for width in range(1, n+1):
            for i in range(n-width+1):
                if width == 1:
                    dp[i][i+width-1] = 1
                elif s[i] == s[i+width-1]:
                    dp[i][i+width-1] = 2 + dp[i+1][i+width-2]
                else:
                    dp[i][i+width-1] = max(dp[i+1][i+width-1], dp[i][i+width-2])
        return dp[0][-1] >= n - k

