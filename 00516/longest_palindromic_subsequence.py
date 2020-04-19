
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        #### [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

        Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

        **Example 1:**
         Input:

        ```
        "bbbab"
        ```

        Output:

        ```
        4
        ```

        One possible longest palindromic subsequence is "bbbb".



        **Example 2:**
         Input:

        ```
        "cbbd"
        ```

        Output:

        ```
        2
        ```

        One possible longest palindromic subsequence is "bb".

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.longestPalindromeSubseq('bbbab')
        4
        >>> sol.longestPalindromeSubseq('cbbd')
        2

        Notes
        -----

        References
        ---------

        """
        d = {}

        def dp(s):
            if s not in d:
                max_len = 0
                for c in set(s):
                    l, r = s.find(c), s.rfind(c)
                    max_len = max(max_len, 1 if l == r else 2+dp(s[l+1:r]))
                d[s] = max_len
            return d[s]

        return dp(s)
