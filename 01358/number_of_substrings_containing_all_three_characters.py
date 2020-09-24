
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        ### [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

        Given a string `s` consisting only of characters *a*, *b* and *c*.

        Return the number of substrings containing **at least** one occurrence of all these characters *a*, *b* and *c*.



        **Example 1:**

        ```
        Input: s = "abcabc"
        Output: 10
        Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
        ```

        **Example 2:**

        ```
        Input: s = "aaacb"
        Output: 3
        Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
        ```

        **Example 3:**

        ```
        Input: s = "abc"
        Output: 1
        ```



        **Constraints:**

        - `3 <= s.length <= 5 x 10^4`
        - `s` only consists of *a*, *b* or *c* characters.


        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.numberOfSubstrings('abcabc')
        10

        Notes
        -----

        References
        ---------

        """
        count = {c: 0 for c in 'abc'}
        i = res = 0
        for j in range(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res
