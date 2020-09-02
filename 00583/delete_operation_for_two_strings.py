from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        #### [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

        Given two words *word1* and *word2*, find the minimum number of steps required to make *word1* and *word2* the same, where in each step you can delete one character in either string.

        **Example 1:**

        ```
        Input: "sea", "eat"
        Output: 2
        Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
        ```



        **Note:**

        1. The length of given words won't exceed 500.
        2. Characters in given words can only be lower-case letters.


        Parameters
        ----------
        word1: str
        word2: str

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return m + n - 2 * dp[-1][-1]
