
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        #### [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/)

        Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

        **Example 1:**

        ```
        Input: num1 = "2", num2 = "3"
        Output: "6"
        ```

        **Example 2:**

        ```
        Input: num1 = "123", num2 = "456"
        Output: "56088"
        ```

        **Note:**

        1. The length of both `num1` and `num2` is < 110.
        2. Both `num1` and `num2` contain only digits `0-9`.
        3. Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.
        4. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.


        Parameters
        ----------
        num1: str
        num2: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.multiply('2', '3')
        '6'
        >>> sol.multiply('123', '456')
        '56088'

        Notes
        -----

        References
        ---------

        """
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = [ord(n)-ord('0') for n in num1][::-1]
        num2 = [ord(n)-ord('0') for n in num2][::-1]

        ans = [0 for _ in range(len(num1)+len(num2))]
        for i, a in enumerate(num1):
            for j, b in enumerate(num2):
                ans[i+j] += a*b
                carry, val = divmod(ans[i+j], 10)
                ans[i+j+1] += carry
                ans[i+j] = val
        ans = ans[::-1]
        pt = 0
        while pt < len(ans) and ans[pt] == 0:
            pt += 1
        return ''.join(map(str, ans[pt:]))

