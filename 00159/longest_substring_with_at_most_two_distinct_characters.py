

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        #### [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

        Given a string ***s*** , find the length of the longest substring ***t*** that contains **at most** 2 distinct characters.

        **Example 1:**

        ```
        Input: "eceba"
        Output: 3
        Explanation: t is "ece" which its length is 3.
        ```

        **Example 2:**

        ```
        Input: "ccaabbb"
        Output: 5
        Explanation: t is "aabbb" which its length is 5.
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
        from collections import OrderedDict
        i, max_len = 0, 0
        d = OrderedDict()
        for j, c in enumerate(s, 1):
            d[c] = j
            d.move_to_end(c)
            if len(d) >= 3:
                _, i = d.popitem(last=False)
            max_len = max(max_len, j-i)
        return max_len
