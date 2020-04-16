

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        #### [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

        Given a string and an integer k, you need to reverse the first k  characters for every 2k characters counting from the start of the  string. If there are less than k characters left, reverse all of them.  If there are less than 2k but greater than or equal to k characters,  then reverse the first k characters and left the other as original.

        **Example:**

        ```
        Input: s = "abcdefg", k = 2
        Output: "bacdfeg"
        ```

        Parameters
        ----------
        s: str
        k: int

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.reverseStr('abcdefg', 2)
        'bacdfeg'

        Notes
        -----

        References
        ---------

        """
        return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:], k) if s else ''


