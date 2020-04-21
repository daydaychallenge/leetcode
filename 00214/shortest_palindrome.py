
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        #### [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)

        Given a string ***s***, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

        **Example 1:**

        ```
        Input: "aacecaaa"
        Output: "aaacecaaa"
        ```

        **Example 2:**

        ```
        Input: "abcd"
        Output: "dcbabcd"
        ```

        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.shortestPalindrome('aacecaaa')
        'aaacecaaa'
        >>> sol.shortestPalindrome('abcd')
        'dcbabcd'

        Notes
        -----

        References
        ---------

        """
        b, mod = 29, 10000000007
        hash1, hash2 = 0, 0
        power = 1
        pos = -1
        for i, c in enumerate(s):
            num = ord(c)-ord('a')+1
            hash1 = (hash1*b + num) % mod
            hash2 = (num*power + hash2) % mod
            if hash1 == hash2:
                pos = i
            power = (power * b) % mod
        return s[pos+1:][::-1] + s
