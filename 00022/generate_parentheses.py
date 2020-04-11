from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        #### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

        Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        For example, given *n* = 3, a solution set is:

        ```
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
        ```

        Parameters
        ----------
        n: int

        Returns
        -------
        List[str]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.generateParenthesis(3)
        ['()()()','()(())','(())()','(()())','((()))']

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
        .. [2] https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
        .. [3] https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation

        """
        res = []

        def gen(left, right, p=''):
            if left == n and right == n:
                res.append(p)
                return

            if left < n:
                gen(left+1, right, p+'(')
            if right < left:
                gen(left, right+1, p+')')

        gen(0, 0)
        return res

    def generateParenthesis01(self, n):
        dp = [[] for _ in range(n+1)]
        dp[0] = ['']
        for i in range(n+1):
            for j in range(i):
                dp[i] += [f'({x}){y}' for x in dp[j] for y in dp[i-j-1]]
        return dp[n]

