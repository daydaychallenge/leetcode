from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        #### [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses)

        Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

        **Example 1:**

        ```
        Input: "(()"
        Output: 2
        Explanation: The longest valid parentheses substring is "()"
        ```

        **Example 2:**

        ```
        Input: ")()())"
        Output: 4
        Explanation: The longest valid parentheses substring is "()()"
        ```

        Parameters
        ----------
        s: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.longestValidParentheses('(()')
        2
        >>> sol.longestValidParentheses(')()())')
        4

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode/
        .. [2] https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack

        """
        stack, s = [0], ')'+s
        res = 0
        for i in range(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i-stack[-1])
            else:
                stack.append(i)
        return res

