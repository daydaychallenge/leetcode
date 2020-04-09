from typing import List


class Solution:
    def rotatedDigits(self, N: int) -> int:
        """
        #### [788. Rotated Digits](https://leetcode.com/problems/rotated-digits)

        X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X. Each digit must be rotated - we cannot choose to leave it alone.

        A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

        Now given a positive number `N`, how many numbers X from `1` to `N` are good?

        ```
        Example:
        Input: 10
        Output: 4
        Explanation:
        There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
        Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
        ```

        **Note:**

        - N will be in range `[1, 10000]`.

        Parameters
        ----------
        N: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.rotatedDigits(10)
        4

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/rotated-digits/discuss/116539/Easy-to-understand-Python-Solution-(using-String)
        .. [2] https://leetcode.com/problems/rotated-digits/discuss/116530/O(logN)-Time-O(1)-Space
        .. [3] http://www.frankmadrid.com/ALudicFallacy/2018/02/28/rotated-digits-leet-code-788/

        """
        skips, remains = '347', '2569'
        count = 0
        for i in map(str, range(1, N+1)):
            if any(c in skips for c in i):
                continue
            if any(c in remains for c in i):
                count += 1
        return count

    def rotatedDigits01(self, N: int) -> int:
        s1 = set('180')
        s2 = set('1802569')

        def isGood(n):
            s = set(str(n))
            return s.issubset(s2) and not s.issubset(s1)
        return sum([isGood(n) for n in range(1, N+1)])








