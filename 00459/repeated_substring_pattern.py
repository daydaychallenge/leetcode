

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        #### [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

        Given a  non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may  assume the given string consists of lowercase English letters only and  its length will not exceed 10000.



        **Example 1:**

        ```
        Input: "abab"
        Output: True
        Explanation: It's the substring "ab" twice.
        ```

        **Example 2:**

        ```
        Input: "aba"
        Output: False
        ```

        **Example 3:**

        ```
        Input: "abcabcabcabc"
        Output: True
        Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
        ```

        Notes
        -----

        References
        ---------

        """
        if not s:
            return False
        n = len(s)
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            j = dp[i-1]
            while j > 0 and s[j] != s[i]:
                j = dp[j-1]
            if s[j] == s[i]:
                j += 1
            dp[i] = j
        last = dp[-1]
        return last and n % (n - last) == 0
