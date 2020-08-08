
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        #### [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

        Given a non-empty string `s`, you may delete **at most** one character.  Judge whether you can make it a palindrome.

        **Example 1:**

        ```
        Input: "aba"
        Output: True
        ```



        **Example 2:**

        ```
        Input: "abca"
        Output: True
        Explanation: You could delete the character 'c'.
        ```



        **Note:**

        1. The string will only contain lowercase characters a-z. The maximum length of the string is 50000.



        Parameters
        ----------
        s: str

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.validPalindrome('aba')
        True
        >>> sol.validPalindrome('abca')
        True

        Notes
        -----

        References
        ---------

        """
        j = 0
        while j < len(s)//2 and s[j] == s[~j]:
            j += 1
        s = s[j:~j+1+len(s)]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
