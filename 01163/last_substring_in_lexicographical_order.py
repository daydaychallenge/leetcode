
class Solution:
    def lastSubstring(self, s: str) -> str:
        """
        ### [1163. Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/)

        Given a string `s`, return the last substring of `s` in lexicographical order.



        **Example 1:**

        ```
        Input: "abab"
        Output: "bab"
        Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
        ```

        **Example 2:**

        ```
        Input: "leetcode"
        Output: "tcode"
        ```



        **Note:**

        1. `1 <= s.length <= 4 * 10^5`
        2. s contains only lowercase English letters.


        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.lastSubstring('abab')
        'bab'
        >>> sol.lastSubstring('leetcode')
        'tcode'

        Notes
        -----

        References
        ---------

        """
        i, j = 0, 1
        k = 0
        while j + k < len(s):
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j += k + 1
            else:
                i = max(i+k+1, j)
                j = i + 1
            k = 0
        return s[i:]

