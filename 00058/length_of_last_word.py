
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        #### [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

        Given a string *s* consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

        If the last word does not exist, return 0.

        **Note:** A word is defined as a **maximal substring** consisting of non-space characters only.

        **Example:**

        ```
        Input: "Hello World"
        Output: 5
        ```

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
        res = s.split()
        if not res:
            return 0
        return len(res[-1])

    def lengthOfLastWordV01(self, s: str) -> int:
        p = len(s)-1
        while p >= 0 and s[p] == ' ':
            p -= 1
        length = 0
        while p >= 0 and s[p] != ' ':
            p, length = p-1, length+1
        return length
