
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        #### [415. Add Strings](https://leetcode.com/problems/add-strings/)

        Given two non-negative integers `num1` and `num2` represented as string, return the sum of `num1` and `num2`.

        **Note:**

        1. The length of both `num1` and `num2` is < 5100.
        2. Both `num1` and `num2` contains only digits `0-9`.
        3. Both `num1` and `num2` does not contain any leading zero.
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

        Notes
        -----

        References
        ---------

        """
        len1, len2 = len(num1), len(num2)
        ans = ['' for _ in range(1+max(len1, len2))]
        ans[:len1] = num1[::-1]
        num2 = num2[::-1]
        carry = i = 0
        while i < len2 or carry:
            carry += int(num2[i]) if i < len2 else 0
            carry += int(ans[i]) if ans[i] else 0
            carry, val = divmod(carry, 10)
            ans[i] = str(val)
            i += 1
        return ''.join(ans[::-1])
