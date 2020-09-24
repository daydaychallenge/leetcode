
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        ### [1328. Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/)

        Given a palindromic string `palindrome`, replace **exactly one** character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that **isn't** a palindrome.

        After doing so, return the final string. If there is no way to do so, return the empty string.



        **Example 1:**

        ```
        Input: palindrome = "abccba"
        Output: "aaccba"
        ```

        **Example 2:**

        ```
        Input: palindrome = "a"
        Output: ""
        ```

        **Constraints:**

        - `1 <= palindrome.length <= 1000`
        - `palindrome` consists of only lowercase English letters.


        Parameters
        ----------
        palindrome: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.breakPalindrome('acbbca')
        'aabbca'
        >>> sol.breakPalindrome('a')
        ''

        Notes
        -----

        References
        ---------

        """
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''

    def breakPalindrome01(self, p: str) -> str:
        return min((p[:i]+'ba'[c > 'a']+p[i+1:] for i, c in enumerate(p) if i*2 != len(p)-1), default='')
