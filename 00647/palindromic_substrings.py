
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        #### [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

        Given a string, your task is to count how many palindromic substrings in this string.

        The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

        **Example 1:**

        ```
        Input: "abc"
        Output: 3
        Explanation: Three palindromic strings: "a", "b", "c".
        ```

        **Example 2:**

        ```
        Input: "aaa"
        Output: 6
        Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
        ```

        **Note:**

        1. The input string length won't exceed 1000.


        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.countSubstrings('abc')
        3
        >>> sol.countSubstrings('aaa')
        6

        Notes
        -----

        References
        ---------

        """
        s = '^#' + '#'.join(s) + '#$'
        r = [0 for _ in range(len(s))]
        center = right = 0
        for i in range(1, len(s)-1):
            if i < right:
                r[i] = min(right-i, r[2*center-i])
            while s[i+r[i]+1] == s[i-r[i]-1]:
                r[i] += 1
            if i + r[i] > right:
                center = i
                right = i + r[i]
        return sum([(v+1)//2 for v in r])




