from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        #### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

        Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

        An input string is valid if:

        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

        Note that an empty string is also considered valid.

        **Example 1:**

        ```
        Input: "()"
        Output: true
        ```

        **Example 2:**

        ```
        Input: "()[]{}"
        Output: true
        ```

        **Example 3:**

        ```
        Input: "(]"
        Output: false
        ```

        **Example 4:**

        ```
        Input: "([)]"
        Output: false
        ```

        **Example 5:**

        ```
        Input: "{[]}"
        Output: true
        ```

        Parameters
        ----------
        s: str

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.isValid('()[]{}')
        True
        >>> sol.isValid('(]')
        False
        >>> sol.isValid('([)]')
        False

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/valid-parentheses/discuss/9271/My-python-solution
        .. [2] https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack

        """
        pairs = {'[': ']', '(': ')', '{': '}'}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack or pairs[stack.pop()] != c:
                return False
        return not stack
