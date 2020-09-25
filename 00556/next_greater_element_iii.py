

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        #### [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/)

        Given a positive **32-bit** integer **n**, you need to find the smallest **32-bit** integer which has exactly the same digits existing in the integer **n** and is greater in value than n. If no such positive **32-bit** integer exists, you need to return -1.

        **Example 1:**

        ```
        Input: 12
        Output: 21
        ```

        **Example 2:**

        ```
        Input: 21
        Output: -1
        ```
        ----------
        n: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.nextGreaterElement(12)
        21

        Notes
        -----

        References
        ---------

        """
        s = list(str(n))
        i = len(s) - 2
        while i >= 0 and s[i] > s[i+1]:
            i -= 1

        if i < 0:
            return -1
        j = i + 1
        while j < len(s) and s[j] >= s[i]:
            j += 1
        s[i], s[j-1] = s[j-1], s[i]
        s[i+1:] = s[i+1:][::-1]
        n = int(''.join(s))
        return n if n < 0x7fffffff else -1
