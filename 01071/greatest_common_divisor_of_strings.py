

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        ### [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

        For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (`t` concatenated with itself 1 or more times)

        Given two strings str1 and str2, return the largest string `x` such that `x` divides both `str1` and `str2`.



        **Example 1:**

        ```
        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"
        ```

        **Example 2:**

        ```
        Input: str1 = "ABABAB", str2 = "ABAB"
        Output: "AB"
        ```

        **Example 3:**

        ```
        Input: str1 = "LEET", str2 = "CODE"
        Output: ""
        ```

        **Example 4:**

        ```
        Input: str1 = "ABCDEF", str2 = "ABC"
        Output: ""
        ```



        **Constraints:**

        - `1 <= str1.length <= 1000`
        - `1 <= str2.length <= 1000`
        - `str1` and `str2` consist of English uppercase letters.



        Parameters
        ----------
        str1: str
        str2: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.gcdOfStrings('ABCABC', 'ABC')
        'ABC'
        >>> sol.gcdOfStrings('ABABAB', 'ABAB')
        'AB'

        Notes
        -----

        References
        ---------

        """
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ''
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        if str2[:len(str1)] == str1:
            return self.gcdOfStrings(str2[len(str1):], str1)
        return ''
