
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        #### [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

        Write a function that takes a string as input and reverse only the vowels of a string.

        **Example 1:**

        ```
        Input: "hello"
        Output: "holle"
        ```

        **Example 2:**

        ```
        Input: "leetcode"
        Output: "leotcede"
        ```

        **Note:**
         The vowels does not include the letter "y".

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
        .. [1] https://www.youtube.com/watch?v=MiqoA-yF-0M

        """
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
