

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        #### [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

        Given a string, find the length of the longest substring T that contains at most *k* distinct characters.

        **Example 1:**

        ```
        Input: s = "eceba", k = 2
        Output: 3
        Explanation: T is "ece" which its length is 3.
        ```

        **Example 2:**

        ```
        Input: s = "aa", k = 1
        Output: 2
        Explanation: T is "aa" which its length is 2.
        ```

        Parameters
        ----------
        s: str
        k: int

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
            if len(d) > k:
                _, i = d.popitem(last=False)
            max_len = max(max_len, j-i)
        return max_len

