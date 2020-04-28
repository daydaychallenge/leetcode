

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        #### [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

        Calculate the sum of two integers *a* and *b*, but you are **not allowed** to use the operator `+` and `-`.

        **Example 1:**

        ```
        Input: a = 1, b = 2
        Output: 3
        ```

        **Example 2:**

        ```
        Input: a = -2, b = 3
        Output: 1
        ```

        Parameters
        ----------
        a: int
        b: int

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
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)


