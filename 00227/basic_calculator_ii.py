
class Solution:
    def calculate(self, s: str) -> int:
        """
        #### [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

        Implement a basic calculator to evaluate a simple expression string.

        The expression string contains only **non-negative** integers, `+`, `-`, `*`, `/` operators and empty spaces ` `. The integer division should truncate toward zero.

        **Example 1:**

        ```
        Input: "3+2*2"
        Output: 7
        ```

        **Example 2:**

        ```
        Input: " 3/2 "
        Output: 1
        ```

        **Example 3:**

        ```
        Input: " 3+5 / 2 "
        Output: 5
        ```

        **Note:**

        - You may assume that the given expression is always valid.
        - **Do not** use the `eval` built-in library function.


        Parameters
        ----------
        s: str

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
        stack, op, num = [], '+', 0
        for i, c in enumerate(s):
            if c.isnumeric():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                op, num = c, 0
        return sum(stack)
