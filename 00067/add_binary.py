

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        #### [67. Add Binary](https://leetcode.com/problems/add-binary/)

        Given two binary strings, return their sum (also a binary string).

        The input strings are both **non-empty** and contains only characters `1` or `0`.

        **Example 1:**

        ```
        Input: a = "11", b = "1"
        Output: "100"
        ```

        **Example 2:**

        ```
        Input: a = "1010", b = "1011"
        Output: "10101"
        ```

        **Constraints:**

        - Each string consists only of `'0'` or `'1'` characters.
        - `1 <= a.length, b.length <= 10^4`
        - Each string is either `"0"` or doesn't contain any leading zero.


        Parameters
        ----------
        a: int
        b: int

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
        i, j = len(a)-1, len(b)-1
        res = ''
        carry = 0
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            carry, val = divmod(carry, 2)
            res = str(val) + res
        return res

