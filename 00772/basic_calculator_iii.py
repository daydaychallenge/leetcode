

class Solution:
    def calculate(self, s: str) -> int:
        """
        #### [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)

        Implement a basic calculator to evaluate a simple expression string.

        The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces ` `.

        The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators , open `(` and closing parentheses `)` and empty spaces ` `. The integer division should truncate toward zero.

        You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2147483648, 2147483647]`.

        Some examples:

        ```
        "1 + 1" = 2
        " 6-4 / 2 " = 4
        "2*(5+5*2)/3+(6/2+8)" = 21
        "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
        ```



        **Note:** **Do not** use the `eval` built-in library function.



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
        op, num, i = '+', 0, 0
        stack = []
        while i < len(s):
            if s[i].isalnum():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                cnt = 1
                j = i
                while cnt != 0:
                    if s[i+1] == '(':
                        cnt += 1
                    if s[i+1] == ')':
                        cnt -= 1
                    i += 1
                num = self.calculate(s[j+1:i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                op = s[i]
                num = 0
            i += 1
        return sum(stack)
