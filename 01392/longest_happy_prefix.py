

class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        #### [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)

        A string is called a *happy prefix* if is a **non-empty** prefix which is also a suffix (excluding itself).

        Given a string `s`. Return the **longest happy prefix** of `s` .

        Return an empty string if no such prefix exists.



        **Example 1:**

        ```
        Input: s = "level"
        Output: "l"
        Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
        ```

        **Example 2:**

        ```
        Input: s = "ababab"
        Output: "abab"
        Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
        ```

        **Example 3:**

        ```
        Input: s = "leetcodeleet"
        Output: "leet"
        ```

        **Example 4:**

        ```
        Input: s = "a"
        Output: ""
        ```



        **Constraints:**

        - `1 <= s.length <= 10^5`
        - `s` contains only lowercase English letters.



        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------
        [1] https://leetcode.com/problems/longest-happy-prefix/discuss/547237/JavaPython-Rolling-Hash
        [2] https://leetcode.com/problems/longest-happy-prefix/discuss/547446/C%2B%2BJava-with-picture-incremental-hash-and-KMP
        """
        res = left = right = 0
        mod = 10**9 + 7
        for i in range(len(s)-1):
            left = (left*26 + ord(s[i])) % mod
            right = (ord(s[~i])*pow(26, i, mod) + right) % mod
            if left == right:
                res = i + 1
        return s[:res]
    def longestPrefix_KMP(self, s: str) -> str:
        i, j = 1, 0
        n = len(s)
        dp = [0]*n
        while i < n:
            if s[j] == s[i]:
                j += 1
                dp[i] = j
            elif j > 0:
                j = dp[j-1]
                i -= 1
            i += 1
        return s[:j]

