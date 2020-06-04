
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        #### [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)

        Given *s1*, *s2*, *s3*, find whether *s3* is formed by the interleaving of *s1* and *s2*.

        **Example 1:**

        ```
        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        Output: true
        ```

        **Example 2:**

        ```
        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
        Output: false
        ```

        Parameters
        ----------
        s1: str
        s2: str
        s3: str

        Returns
        -------
        bool

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/4298664.html

        """
        rows, cols = len(s1), len(s2)
        if rows + cols != len(s3):
            return False
        dp = [[False for _ in range(cols+1)] for _ in range(rows+1)]
        dp[0][0] = True
        for i in range(1, rows+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, cols+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]

    def isInterleaveV01(self, s1: str, s2: str, s3: str) -> bool:
        rows, cols = len(s1), len(s2)
        if rows + cols != len(s3):
            return False
        dp = [False for _ in range(cols+1)]
        dp[0] = True
        for j in range(1, cols+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
        return dp[-1]


