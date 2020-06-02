
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        #### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

        Given two strings *s* and *t* , write a function to determine if *t* is an anagram of *s*.

        **Example 1:**

        ```
        Input: s = "anagram", t = "nagaram"
        Output: true
        ```

        **Example 2:**

        ```
        Input: s = "rat", t = "car"
        Output: false
        ```

        **Note:**
         You may assume the string contains only lowercase alphabets.

        **Follow up:**
         What if the inputs contain unicode characters? How would you adapt your solution to such case?


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

        """
        from collections import Counter
        counts = Counter(s)
        for c in t:
            counts[c] -= 1
        return all(x==0 for x in counts.values())
