from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        ### [186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)

        Given an input string , reverse the string word by word.

        **Example:**

        ```
        Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
        ```

        **Note:**

        - A word is defined as a sequence of non-space characters.
        - The input string does not contain leading or trailing spaces.
        - The words are always separated by a single space.

        **Follow up:** Could you do it *in-place* without allocating extra space?

        Parameters
        ----------
        s: List[str]

        Returns
        -------
        None

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        reverse(s, 0, len(s)-1)

        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverse(s, start, end-1)
                start = end+1
            elif end == len(s)-1:
                reverse(s, start, end)

