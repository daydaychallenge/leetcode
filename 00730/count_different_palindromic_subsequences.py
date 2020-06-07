
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        """
        #### [730. Count Different Palindromic Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/)

        Given a string S, find the number of different non-empty palindromic subsequences in S, and **return that number modulo `10^9 + 7`.**

        A subsequence of a string S is obtained by deleting 0 or more characters from S.

        A sequence is palindromic if it is equal to the sequence reversed.

        Two sequences `A_1, A_2, ...` and `B_1, B_2, ...` are different if there is some `i` for which `A_i != B_i`.

        **Example 1:**

        ```
        Input:
        S = 'bccb'
        Output: 6
        Explanation:
        The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
        Note that 'bcb' is counted only once, even though it occurs twice.
        ```



        **Example 2:**

        ```
        Input:
        S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
        Output: 104860361
        Explanation:
        There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
        ```


        **Note:**

        The length of `S` will be in the range `[1, 1000]`.

        Each character `S[i]` will be in the set `{'a', 'b', 'c', 'd'}`.



        Parameters
        ----------
        S: str

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=UjiFFYU3EKM

        """
        slen, mod = len(S), 10**9+7
        dp = [[0 for _ in range(slen)] for _ in range(slen)]
        for distance in range(1, slen):
            for i in range(slen-distance):
                j = i + distance
                if S[i] == S[j]:
                    left, right = i+1, j-1
                    while S[left] != S[i]:
                        left += 1
                    while S[right] != S[i]:
                        right -= 1
                    if left > right:
                        dp[i][j] = 2*dp[i+1][j-1] + 2
                    elif left < right:
                        dp[i][j] = 2*dp[i+1][j-1]-dp[left+1][right-1]
                    else:
                        dp[i][j] = 2*dp[i+1][j-1] + 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            dp[i][j] %= mod
        return dp[0][-1]

