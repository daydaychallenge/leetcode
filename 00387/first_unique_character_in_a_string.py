
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        ####  [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

        **Examples:**

        ```
        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
        ```

        **Note:** You may assume the string contain only lowercase English letters.


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
        from collections import Counter
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1

