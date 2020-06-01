
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        #### [161. One Edit Distance](https://leetcode.com/problems/one-edit-distance/)

        Given two strings s and t, determine if they are both one edit distance apart.

        **Note:**

        There are 3 possiblities to satisify one edit distance apart:

        1. Insert a character into s to get t
        2. Delete a character from s to get t
        3. Replace a character of s to get t

        **Example 1:**

        ```
        Input: s = "ab", t = "acb"
        Output: true
        Explanation: We can insert 'c' into s to get t.
        ```

        **Example 2:**

        ```
        Input: s = "cab", t = "ad"
        Output: false
        Explanation: We cannot get t from s by only one step.
        ```

        **Example 3:**

        ```
        Input: s = "1203", t = "1213"
        Output: true
        Explanation: We can replace '0' with '1' to get t.
        ```


        Parameters
        ----------
        s: str
        t: str

        Returns
        -------
        bool

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/one-edit-distance/discuss/50095/Python-concise-solution-with-comments.

        """
        lens, lent = len(s), len(t)
        if lens > lent:
            return self.isOneEditDistance(t, s)
        if lent - lens > 1 or s == t:
            return False

        for i in range(lens):
            if t[i] != s[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
        return True
